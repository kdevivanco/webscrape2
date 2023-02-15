For this task, I had to scrape a webpage and translate its content to another language. Here's how I did it. 

Script I used to translate text from the DOM using the Google Translate API. 

Translating script: 

<script type="text/javascript">
    const translate = async (text) => {
      const sourceLang = 'en'; //Source language / original language - autodetect is an option too.
      const targetLang = 'hi'; //Target language to translate 
      const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${sourceLang}&tl=${targetLang}&dt=t&q=${encodeURI(text)}`;

      const response = await fetch(url);
      const data = await response.json();

      if (data[0][0][0]) {
        return data[0][0][0];
      } else {
        return text;
      }
    };


    let elements = document.querySelectorAll('head title, strong, .translate, h2.head-2, h3.text-1, h3.text-2, h3.head-2, body span, body button,p, footer a, a.link-gray-underline');
    for (let element of elements) {
      if (element.innerText) {
        const originalText = element.innerText
        translate(originalText.toString())
          .then((translatedText) => {
            element.innerText = translatedText;
          })
          .catch((error) => {
            console.error(error);
            element.innerText = originalText;
          });
      }
    }

  </script>


Script to automate inserting text (script) into HTML using Python:

Required: 
import os
import pdb

js_script = '''script or whatever you want to insert'''
 
to_replace='''what ever you want to replace!'''

def add_to_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            # Open the file and read its content
            with open(file_path, "r") as f:
                content = f.read()
            # Append your code to the content
            content = content.replace(to_replace, js_script)
            # Write the updated content back to the file
            with open(file_path, "w") as f:
                f.write(content)


Code by: Kayla de Vivanco


