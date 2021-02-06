from keras import backend as K

def r(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def p(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1_m(y_true, y_pred):
    precision = r(y_true, y_pred)
    recall = r(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc',f1_m,p,r])

history = model.fit(X, y, epochs=epochs, batch_size=batch_size)

# evaluate the model
print(model.evaluate(X, y, verbose=0),type(model.evaluate(X, y, verbose=0)))
loss, accuracy, f1_score, p, r = model.evaluate(X, y, verbose=0)

#accuracy = model.evaluate(X, y)
ic(loss, accuracy, f1_score, p, r)