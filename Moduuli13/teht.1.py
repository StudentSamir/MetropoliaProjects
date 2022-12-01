from flask import Flask

app = Flask(__name__)


@app.route("/alkuluku/<int:number>")
def prime(number):

    isPrime = True
    if number >= 1:
        for n in range(2, number):
            if number % n == 0:
                print(f"{number}" + "is a prime number")
                break

    else:
        print(f"{number}" + "is not a prime number")
        isPrime = False


    answer = {
        "number": number,
        "isPrime": isPrime
    }

    return answer

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
