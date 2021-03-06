from poutyne import Model

model = Model(network, 'sgd', 'cross_entropy',
                batch_metrics=['accuracy'], epoch_metrics=['f1'])
model.to(device)

model.fit_generator(train_loader, valid_loader,
                    epochs=num_epochs, callbacks=callbacks)

test_loss, (test_acc, test_f1) = model.evaluate_generator(test_loader)
print(f'Test: Loss: {test_loss}, Accuracy: {test_acc}, F1: {test_f1}')
