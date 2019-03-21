---

# Nagoya castle or not

名古屋城なのか

---

# These slides are at Connpass. So, you can check them out.

スライドはConnpassにアップされています。是非みてください。

---

# On Connpass, I'm "globophobe".

Connpassでは、私は「globophobe」です。
![](https://raw.githubusercontent.com/globophobe/nagoya-castle-or-not/master/slides/img/arex.png)

---
# Last year, at Python Tokai at Nagoya castle, someone did a LT about something related to classification of images of Nagoya castle. 

昨年、名古屋城で開催されたPython東海で、名古屋城の画像の分類に関連するLTがありました。

---

# I thought it was a little hard.

少し難しいと思いました。

---

# Recently, I finished [Fast.ai](https://course.fast.ai/version 3) lesson 1 & 2.

最近、私はFast.aiバージョン3のレッスン1と2を終えました。

---

# In lesson 1, there was an example, "baseball" or "cricket".

レッスン1では、「野球」または「クリケット」の例がありました。

---

# It was trained with 30 images.

それは30の画像で訓練されました。

---

![](https://raw.githubusercontent.com/hiromis/notes/master/lesson1/6.png)

---

# So, I decided to make a classifier for Nagoya castle, Osaka castle, and Kumamoto castle.

それで、名古屋城、大阪城、それとも熊本城の分類器を作ることにしました。

---

# I put it in a docker container, and uploaded it to Google Compute Engine.

dockerのコンテナーを作って、Google Compute Engineにアップしました。

[Click here](http://35.221.88.219/)
[ここをクリック](http://35.221.88.219/)

---

# Dockerfile and source code is on [github](https://github.com/globophobe/nagoya-castle-or-not).

Dockerfileとソースコードは[github](https://github.com/globophobe/nagoya-castle-or-not)にあります。

---

![](https://upload.wikimedia.org/wikipedia/commons/1/1d/080405_nagoya_csl_sakura.JPG)

Nagoya castle?

[Click here](http://35.221.88.219/classify-url?url=https://upload.wikimedia.org/wikipedia/commons/1/1d/080405_nagoya_csl_sakura.JPG)
[ここをクリック](http://35.221.88.219/classify-url?url=https://upload.wikimedia.org/wikipedia/commons/1/1d/080405_nagoya_csl_sakura.JPG)

---

![](https://upload.wikimedia.org/wikipedia/commons/3/38/Matsumoto_Castle05s5s4592.jpg)

Nagoya castle?

[Click here](http://35.221.88.219/classify-url?url=https://upload.wikimedia.org/wikipedia/commons/3/38/Matsumoto_Castle05s5s4592.jpg)

[ここをクリック](http://35.221.88.219/classify-url?url=https://upload.wikimedia.org/wikipedia/commons/3/38/Matsumoto_Castle05s5s4592.jpg)

---

# Its's Matsumoto castle. The classifier wasn’t trained to recognize it.
それが松本城でした。 分類器はそれを認識するように訓練されていませんでした。

---

# More about this later.
それについてもう少し後で。

---

# What is Fast.ai?

Fast.aiて何？

---

# It's a free deep learning curriculum.

無料機械学習カリキュラムです。

---

# The teacher was Kaggle #1.

先生はKaggleの位１でした。
![](https://raw.githubusercontent.com/hiromis/notes/master/lesson1/2.png)

---

# Fast.ai has 4 courses. The first is "Practical Deep Learning for Coders".

Fast.aiには4つのコースがあります。最初のコースは「実践的なディープラーニング」です。

---

# Lesson 1 and 2 explains to create a CNN with ResNet for transfer learning, and train with 1 cycle policy.

レッスン1と2では、ResNetを使用してトランスファーラーニング用にCNNを作成し、1サイクルポリシーでトレーニングをするについて説明します。

---

# "One cycle learning" is explained in a paper that was released in April 2018.

「1サイクル学習」は、2018年4月に発表された論文で説明されています。

[Click here](https://arxiv.org/abs/1803.09820)
[ここをクリック](https://arxiv.org/abs/1803.09820)

---

# I would be thankful, if a smarter person can explain "one cycle learning"

もっと賢い人が「1サイクル機械学習」を説明出来ればありがたいです。

---

# In essence, it’s fast.
要するに、それは速いです。

---

# I decided to use Google Colaboratory for the Fast.ai course.

Fast.aiコースにGoogle Colaboratoryを使用することにしました。

---

# Google Colaboratory has support for Fast.ai

Google ColaboratoryはFast.aiをサポートしています。

![](https://raw.githubusercontent.com/globophobe/nagoya-castle-or-not/master/slides/img/colaboratory-fastai-v3.png)

---

# I used Google Drive to store the training data.

Google Driveを使用してトレーニングデータを保存しました。

---

# Let's have a look.

みてみましょう。

---

# That’s all. Thanks for listening.

以上です。ご清聴ありがとうございます。
