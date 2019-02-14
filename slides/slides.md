---

# 名古屋城なのか
## Nagoya castle or not

---

These slides are already uploaded to Connpass.
これらのスライドはすでにConnpassにアップロードされています。

---

Last year, at the Python Tokai at Nagoya castle, someone did an LT about something related to classification of images of Nagoya castle. 

昨年、名古屋城で開催されたPython東海で、名古屋城の画像の分類に関連するLTがありました。

---

I thought it was a little hard.

少し難しいと思いました。

---

Recently, I finished [Fast.ai](https://course.fast.ai/ version 3) lesson 1 & 2.

最近、私はFast.aiバージョン3のレッスン1と2を終えました。

---

In lesson 1, there was an example, "baseball" or "cricket".

レッスン1では、「野球」または「クリケット」の例がありました。

It was trained with 30 images.

それは30の画像で訓練されました。

---

![](https://github.com/hiromis/notes/blob/master/lesson1/6.png)

---

So, I decided to make a classifier for Nagoya castle, Osaka castle, and Kumamoto castle.

それで、名古屋城、大阪城、それとも熊本城の分類器を作ることにしました。

---

# The result:
## その結果は：

I uploaded it to Google Compute Engine in a docker container.

私はdockerのコンテナーでGoogle Compute Engineにそれをアップロードしました。

[Click here](http://35.221.88.219/)
ここをクリック

---

What is Fast.ai?

Fast.aiてなに？

---

It's a free deep learning course taught by Jeremy Howard. 

それはHoward Jeremyさんが教えられた無料機械学習コースです。

---

https://github.com/hiromis/notes/blob/master/lesson1/2.png

以前、Kaggleの位１になった方です。

---

Fast.ai has 4 courses, the first is "Practical Deep Learning for Coders".

Fast.aiには4つのコースがあり、最初のコースは「実践的なディープラーニング」です。

---

Jeremy Howard says, "The...focus of the whole course...is how to do...'transfer learning.'" 

Howardさんは「コース全体の焦点は、転送学習のやり方です」

---

Lesson 1 explains to create a CNN with ResNet, and train with fit_one_cycle.

レッスン1では、ResNetを使用してCNNを作成し、fit_one_cycleを使用してトレーニングする方法について説明します。

---

"One cycle learning" is explained in a paper that was released in April 2018.

「1サイクル学習」は、2018年4月に発表された論文で説明されています。

[Click here](https://arxiv.org/abs/1803.09820)

---

I would be thankful, if a smarter person can explain "one cycle learning"

もっと賢い人が「1サイクル機械学習」を説明できたらありがたいです。

---

I decided to use Google Colaboratory for the Fast.ai course.

Fast.aiコースにGoogle Colaboratoryを使用することにしました。

---

Google Colaboratory has support for Fast.ai

Google ColaboratoryはFast.aiをサポートしています。

[Click here](https://colab.research.google.com/notebooks/welcome.ipynb#github=true)

---

I used Google Drive to store the training data.

Google Driveを使用してトレーニングデータを保存しました。

---

Let's have a look.

みてみましょう。
