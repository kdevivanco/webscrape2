import os
import pdb

js_script = '''</noscript>
  <script type="text/javascript">
    const translate = async (text) => {
      const sourceLang = 'en';
      const targetLang = 'hi';
      const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${sourceLang}&tl=${targetLang}&dt=t&q=${encodeURI(text)}`;

      const response = await fetch(url);
      const data = await response.json();

      if (data[0][0][0]) {
        return data[0][0][0];
      } else {
        return text;
      }
    };


    let elements = document.querySelectorAll('body strong, h1, a, body span, body h2, body h3, body button,p, footer a, a.link-gray-underline a.site-header__navigation-action, a.site-header__navigation-submenu-action');
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
</script>'''
 
to_replace='</noscript>'

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


# # The parent directory containing the child directories with index.html files
# parent_directory = "/Users/macbookpro/Desktop/Programacion/AllStars2/www.classcentral.com/report"

# # Walk through the directory tree
# for root, dirs, files in os.walk(parent_directory):
#     for file in files:
#         # Check if the file is named index.html
#         if file == "index.html":
#             file_path = os.path.join(root, file)
#             # Open the file and read its content
#             with open(file_path, "r") as f:
#                 content = f.read()
#             # Append your code to the content
#             content = content.replace(old_text, new_text)
#             # Write the updated content back to the file
# #             with open(file_path, "w") as f:
#                 f.write(content)

pdb.set_trace()