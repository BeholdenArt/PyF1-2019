import numpy as np
from alexnet import alexnet

WIDTH = 100
HEIGHT = 80
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'F12019-Mercedes-{}-{}-{}-{}-epochs.model'.format("Britain", LR, 'alexnetv2',EPOCHS)
model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('Training-Data-222K-Britain-Balanced.npy', allow_pickle= True)
train = train_data[:-50]
test = train_data[-50:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]
testX = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
testY = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, 
	validation_set=({'input': testX}, {'targets': testY}), 
    snapshot_step=1000, show_metric=True, run_id=MODEL_NAME)

# TENSORBOARD LINK : tensorboard --logdir=foo:D:\Code\Projects\AI\PC\F1\log

model.save(MODEL_NAME)