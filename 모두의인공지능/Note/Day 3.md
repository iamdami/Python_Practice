Day 3
===
## A Neural Network Playground  
- [A Neural Network Playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.62073&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)  
- 용어 정리  
  - Learning rate: 오차값 최소화하기 위해 각 뉴런 연결하는 가중치 값 수정해 나감 -> 한 번 수정할 때 얼마만큼 수정할 지 이 값으로 결정  
  - Activation: 활성화 함수 의미. ReLU, tanh, Sigmoid, Linear 함수 사용 가능  
  - Regularization: 정규화 의미. 정규화 목적: 과적합 줄이기  
  *과적합: 모델이 학습된 데이터에는 잘 작동하지만, 이전에 보지 못한 데이터에는 잘 작동하지 않는 것  
  - Regularization rate: 정규화할 때 어느 정도로 값 수정할지 정해줄 때 사용하는 값  
<br>
  
## ANN(Artificial Neural Network)  
- 다양한 딥러닝 기술의 시초  
- [ANN - wikipedia](https://en.wikipedia.org/wiki/Artificial_neural_network)  
<br>
  
## CNN(Convolutional Neural Network)
- 합성곱 신경망  
- 이미지 특성 파악에 특화됨  
- 이미지를 특정한 영역별로 추출해 학습시킴  
- [CNN - Convolutional Neural Network](https://towardsdatascience.com/understanding-cnn-convolutional-neural-network-69fd626ee7d4#:~:text=CNN%20is%20a%20type%20of,features%20automatically%20for%20better%20classification.)  
<br>
  
## RNN(Recurrent neural network)
- 순환 신경망  
- 일반적인 인공신경망(ANN)에서는 신경망의 구성에 따라 가중치가 한 방향으로 이동하며 변하지만  
  순환 신경망에서는 가중치의 변화가 다시 자기 자신에게 돌아오는 형태 가짐(계속 반복적으로 가중치 수정되는 모습 나타남)  
- 연속 데이터에 대한 결과 예측하거나 분류할 때 사용  
- 언어 번역, 시간 흐름, 연속된 관계 가지는 데이터에 대해!  
<br>
  
## sketch-rnn  
- [sketch-rnn](https://magenta.tensorflow.org/assets/sketch_rnn_demo/index.html)  
- 퀵 드로우 데이터 셋  
- 순서 데이터 학습 -> 그림 그리는 과정 예측  
<br>
  
## 생성 신경망 살펴보기  
<br>
  
