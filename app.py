from flask import Flask, render_template,redirect, request
import generate_captions
import generate_captions2
import generate_captions3
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def submit():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        c1 = generate_captions.give_caption(path)
        caption1 = ""
        caption1 += c1[0].upper()
        for i in range(1,len(c1)):
            caption1 += c1[i]
        caption1 += "."

        c2 = generate_captions2.give_caption(path)
        caption2 = ""
        caption2 += c2[0].upper()
        for i in range(1, len(c2)):
            caption2 += c2[i]
        caption2 += "."

        c3 = generate_captions3.give_caption(path)
        caption3 = ""
        caption3 += c3[0].upper()
        for i in range(1, len(c3)):
            caption3 += c3[i]
        caption3 += "."

        result_dic = {
            "image":path,
            'caption1':caption1,
            'caption2': caption2,
            'caption3': caption3
        }
        print(caption1)
        print(caption2)
        print(caption3)
    return render_template("index.html",your_result=result_dic)

if __name__=="__main__":
    app.debug = True
    app.run()