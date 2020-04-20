from flask import Flask, render_template,redirect, request
import generate_captions
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

        c = generate_captions.give_caption(path)
        caption = ""
        caption += c[0].upper()
        for i in range(1,len(c)):
            caption += c[i]
        caption += "."

        result_dic = {
            "image":path,
            'caption':caption
        }
        print(caption)
    return render_template("index.html",your_result=result_dic, file_name=f.filename)
        #print(caption)
    return render_template("index.html",your_result=result_dic, file_name=f.filename)

if __name__=="__main__":
    app.debug = True
    app.run()
