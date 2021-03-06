from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import io
apbot=Flask(__name__)
@apbot.route("/sms", methods=["GET","POST"])
def reply():
    print(request.form)
    num=request.form.get("From").replace("whatsapp:","")
    msg_text=request.form.get("Body")
    count_file=request.form.get("NumMedia")
    if(count_file=="1"):
        file_type=request.form.get("MediaContentType0").split("/")[1]
        if(file_type=="csv"):
            url_file=request.form.get("MediaUrl0")
            msg=MessagingResponse()
            resp=msg.message("valid attachment")
            resp=msg.message(f"you sent {msg_text} from {num},and you attached {file_type} file.File is available in {url_file} ")
            with io.open("file_link.csv","w",encoding="utf-8")as f1:
                f1.write(num+","+url_file)
            return(str(msg))
        else:
            msg=MessagingResponse()
            resp=msg.message("invalid attachment")
            resp=msg.message(f"you sent {msg_text} from {num},and you attached {file_type} file.")
            return(str(msg))
            
        
    else:
        msg=MessagingResponse()
        resp=msg.message(f"you have not attached any thing from {num}")
        return(str(msg))


if __name__=="__main__":
    apbot.run(port=5000)
