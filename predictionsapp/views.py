from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms

import pandas as pd
import numpy as np
from Bio import SeqIO

from keras import preprocessing
from keras.models import load_model
from keras_preprocessing.text import tokenizer_from_json
from venomClassifier import settings
import json 
from os.path import join
from django.contrib.auth.models import User
from .models import Sequences

MAX_LENGHT = 600

@login_required(login_url='Login')
def classifier(request):
    if request.method=='POST':
        form = forms.sequenceForm(request.POST)
        if form.is_valid():
            if request.FILES:
                try:
                    meta=[]
                    sequence=[]
                    for seq_record in SeqIO.parse(request.FILES, "fasta"):
                        meta.append(str(seq_record.description))
                        sequence.append(str(seq_record.seq))
                    df = pd.DataFrame(data ={'Meta':meta,'Sequence':sequence})
                    df['Clasification'] = ''
                    
                    X = np.array(df['Sequence'].tolist())
                except:
                    form = forms.sequenceForm()

                    return render(request, 'predictionsapp/classifier.html', { 'form': form })
            else:
                X = []
                seq = (request.POST)['sequence']
                X.append(seq.upper())
                
            
            with open(join(settings.BASE_DIR, 'predictionsapp/model_config/tokenizer.json')) as f:
                data = json.load(f)
                tokenizer = tokenizer_from_json(data)

            X = tokenizer.texts_to_sequences(X)
            X = preprocessing.sequence.pad_sequences(X, maxlen=MAX_LENGHT, padding='post')
            
            loading_path = join(settings.BASE_DIR, 'predictionsapp/model_config/venom_classifier_model1.h5')
            model = load_model(loading_path)

            predictions = model.predict(x=X, verbose=0)
            rounded_pred = np.argmax(predictions, axis=-1)

            for i in range(len(predictions)):
                prbNotVenom=predictions[i][0]
                prbVenom=predictions[i][1]

                instance = form.save(commit=False)
                instance.probnotvenom = round((prbNotVenom * 100),2)
                instance.probvenom = round((prbVenom * 100),2)
                instance.consultant = request.user
                instance.prediction=rounded_pred[i]
                
                instance.save()

            form=forms.sequenceForm()
        else:
            logUser = (request.user).id
            # instance=[]
            # for i in Sequences.objects.get(consultant_id = logUser):
            #     instance.append(i)
            for instance in Sequences.objects.raw("SELECT ps.id FROM predictionsapp_sequences as ps WHERE consultant_id = {0} ORDER BY date DESC".format(logUser)):
                instance.delete()
            


    else:
        form = forms.sequenceForm()


    logUser = (request.user).id
    predictionsList=[]
    for i in Sequences.objects.raw("SELECT ps.id, ps.sequence, ps.prediction, ps.probnotvenom, ps.probvenom FROM predictionsapp_sequences as ps WHERE consultant_id = {0} ORDER BY date DESC".format(logUser)):
        predictionsList.append(i)
    
    for i in range(len(predictionsList)):
        if len(predictionsList[i].sequence) > 15:
            predictionsList[i].sequence = predictionsList[i].sequence[:15] + '...'
    
    ctx = {'form': form, 'predictionList':predictionsList}

    return render(request, 'predictionsapp/classifier.html', ctx)