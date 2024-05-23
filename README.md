# final_project
Generalization Abilities of Deep Neural Networks

## Prepare
Our environment is Pytorch and torchvision.  Either CPU or GPU is applicable for my experiments.


## SGD v.s. GD
The implementation is the notebook. The house_price dataset is included.

## SGD v.s. Adam
### Generalization Experiments
Please find the test code in the "main.py" file. You can directly run it by selecting SGD or ADAM optimizer.

To obtain the convergence trajectory data of SGD and ADAM, you can directly run "main.py".

For datasets, we can choose MNIST or CIFAR-10. The code can automatically download the dataset.

To show the convergence trajectory of SGD and ADAM in terms of noise and the training/test accuracy, you can directly run "plot_CIFAR10.py".

My running resluts are provided in model/ and log_out/.

## License

This project is under the MIT License. See [LICENSE](LICENSE) for details.
