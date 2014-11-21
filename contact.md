---
layout: page
title: Contact
permalink: /contact/
---

#Contact me
 
<form class="form-horizontal">
<fieldset>

<legend>Drop me an email, I'll respond as soon as possible!</legend>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="email">Email address</label>  
  <div class="col-md-5">
  <input id="email" name="email" type="text" placeholder="Your email address" class="form-control input-md" required="required">
  <span class="help-block">Write your email address here</span>  
  </div>
</div>

<!-- Textarea -->
<div class="form-group">
  <label class="col-md-4 control-label" for="msg">Message</label>
  <div class="col-md-4">                     
    <textarea class="form-control" id="msg" name="msg" placeholder="Your message" cols="40" rows="5" required="required"></textarea>
	 <span class="help-block">Write your message here</span>  
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="btnSend"></label>
  <div class="col-md-4">
    <button id="btnSend" name="btnSend" class="btn btn-primary" onclick="send();">Send</button>
  </div>
</div>

</fieldset>
</form>

<div id="usrMsg">
</div>


 
<script>
function send()
{
	event.preventDefault();
	var sender =$('#email').val();
	var msgtext =$('#msg').val();
	
	if(sender==undefined || sender == '')
	{
		$('#usrMsg').empty().append('<p class="bg-danger">Please specify your email address</p>');
		return;
	}
	
	if(msgtext==undefined || msgtext == '')
	{
		$('#usrMsg').empty().append('<p class="bg-danger">Please write a message</p>');
		return;
	}
	
	console.log("SENDING " + sender + ", " + msgtext);
 var xhr = $.ajax({
      type: 'POST',
      url: "https://mandrillapp.com/api/1.0/messages/send.json",
      dataType: 'json',
      data: {
        key: '-NE8t9pX1PfJsG8uiK_syA',
        message: {
          text: msgtext,
          subject: "New message from trapias.github.io",
          from_email: sender,
          from_name: sender,
          to: [{
                  "email": "trapias@gmail.com",
                  "name": "AL"
              }]
        }
      }
    });
    
    xhr.done(function(data) {
      console.log(JSON.stringify(data));
	  $('#usrMsg').empty().append('<p class="bg-success">Your message has been delivered, thank you.</p>');
    });
    
    xhr.fail(function(jqXHR, textStatus, errorThrown) {
      console.log(jqXHR.responseText);
	  $('#usrMsg').empty().append('<p class="bg-danger">There was an error: ' + jqXHR.responseText + '</p>');
    });
	
}
</script>

