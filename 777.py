from flask import Flask, render_template_string

app = Flask(__name__)

menu = [
    {
        "name": "Burger",
        "price": 120,
        "description": "Beef burger with cheese"
    },
    {
        "name": "Pizza",
        "price": 180,
        "description": "Pepperoni pizza"
    },
    {
        "name": "Pasta",
        "price": 140,
        "description": "Creamy white sauce pasta"
    },
    {
        "name": "Chicken Grill",
        "price": 200,
        "description": "Grilled chicken with fries"
    }
]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Menu</title>

    <style>

        body{
            font-family: Arial;
            background: #111;
            color: white;
            text-align: center;
            padding: 20px;
        }

        h1{
            color: orange;
            margin-bottom: 40px;
        }

        .menu-container{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
        }

        .card{
            background: #222;
            width: 250px;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(255,165,0,0.4);
            transition: 0.3s;
        }

        .card:hover{
            transform: scale(1.05);
        }

        .price{
            color: orange;
            font-size: 22px;
            margin-top: 10px;
        }

    </style>

</head>

<body>

    <h1>🔥 Restaurant Menu 🔥</h1>

    <div class="menu-container">

        {% for item in menu %}

        <div class="card">
            <h2>{{ item.name }}</h2>
            <p>{{ item.description }}</p>
            <div class="price">{{ item.price }} EGP</div>
        </div>

        {% endfor %}

    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html, menu=menu)

if __name__ == '__main__':
    app.run(debug=True)