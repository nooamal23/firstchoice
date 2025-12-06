from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('our-services.html')

@app.route('/gallery')
def gallery():
    return render_template('our-gallery.html')

@app.route('/about_company')
def about_company():
    return render_template('about-company.html')

@app.route('/company_history')
def company_history():
    return render_template('company-history.html')

@app.route('/project')
def project():
    return render_template('our-project-v2.html')

@app.route('/team')
def team():
    return render_template('our-team.html')

@app.route('/faqs')
def faqs():
    return render_template('FAQs.html')

@app.route('/error')
def error():
    return render_template('404.html')

@app.route('/blog')
def blog():
    return render_template('blog-list-v2.html')

@app.route('/appointment')
def appointment():
    return render_template('book-calendar.html')

@app.route('/shop')
def shop():
    return render_template('shop-grid-sidebar-v2.html')

@app.route('/shop_grid_sidebar_v2')
def shop_grid_sidebar_v2():
    return render_template('shop-grid-sidebar-v2.html')

@app.route('/shop_detail_sidebar')
def shop_detail_sidebar():
    return render_template('shop-detail-sidebar.html')

@app.route('/contact')
def contact():
    return render_template('contact-us-v1.html')

@app.route('/blog_single')
def blog_single():
    return render_template('blog-single.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))   # Render gives a random PORT
    app.run(host="0.0.0.0", port=port)