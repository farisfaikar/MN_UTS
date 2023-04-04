"""
Nama: Faris Faikar Razannafi
NIM: 4611421092
Matkul: Metode Numerik
Perihal: UTS
"""
import sympy


def bisection(f, a, b, tol, max_iter=50):
    if f(a) * f(b) > 0:
        print("Tidak ada akar dalam interval yang diberikan.")
        return None
    else:
        print(f"{'n':^5} {'a':^10} {'b':^10} {'c':^10} {'f(a)':^10} {'f(b)':^10} {'f(c)':^10} {'(b-a)/2':^10}")
        n = 1
        error = (b - a) / 2
        running = True
        while (error > tol or running) and n < max_iter:
            if error <= tol:
                running = False
            c = (a + b) / 2
            print(
                f"{n:^5} {a:>10.6f} {b:>10.6f} {c:>10.6f} {f(a):>10.6f} {f(b):>10.6f} {f(c):>10.6f} {error:>10.6f}")
            if f(c) == 0:
                return c
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            n += 1
            error = (b - a) / 2

        print(f"{n:^5} {a:>10.6f} {b:>10.6f} {c:>10.6f} {f(a):>10.6f} {f(b):>10.6f} {f(c):>10.6f} {error:>10.6f}")
        return (a + b) / 2


def regula_falsi(f, a, b, tol, max_iter=50):
    if f(a) * f(b) > 0:
        print("Tidak ada akar dalam interval yang diberikan.")
        return None
    else:
        print(f"{'n':^5} {'a':^10} {'b':^10} {'c':^10} {'f(a)':^10} {'f(b)':^10} {'f(c)':^10} {'|f(b)-f(a)|/|f(a)+f(b)|':^10}")
        n = 1
        error = abs(f(b) - f(a)) / (abs(f(a)) + abs(f(b)))
        while error > tol and n < max_iter:
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))
            print(
                f"{n:^5} {a:>10.6f} {b:>10.6f} {c:>10.6f} {f(a):>10.6f} {f(b):>10.6f} {f(c):>10.6f} {error:>10.6f}")
            if f(c) == 0:
                return c
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            n += 1
            error = abs(f(b) - f(a)) / (abs(f(a)) + abs(f(b)))
        print(f"{n:^5} {a:>10.6f} {b:>10.6f} {c:>10.6f} {f(a):>10.6f} {f(b):>10.6f} {f(c):>10.6f} {error:>10.6f}")
        return (a * f(b) - b * f(a)) / (f(b) - f(a))


def iterasi_titik_tetap(g, x0, tol, max_iter=50):
    print(f"{'n':^5} {'xn':^10} {'xn-1xn':^10}")
    n = 1
    print(f"{n:^5} {x0:^10.6f} {'-':^10}")
    n += 1
    xn = g(x0)
    while abs(xn - x0) > tol and n < max_iter:
        print(f"{n:^5} {xn:^10.6f} {abs(xn - x0):^10.6f}")
        x0 = xn
        xn = g(x0)
        n += 1

    print(f"{n:^5} {xn:^10.6f} {abs(xn - x0):^10.6f}")

    if n == max_iter:
        print("Iterasi tidak konvergen.")
        return None
    else:
        return xn


def newton_rhapson(f, df, x0, tol, max_iter=50):
    print(f"{'n':^5} {'f(xn)':^10} {'f''(xn)':^10} {'xn-xn-1':^10} {'|(xn-xn-1)/xn|':^10}")
    xn = x0 - f(x0) / df(x0)
    n = 1
    while abs(xn - x0) > tol and n < max_iter:
        # TODO: Pake abs()?
        print(
            f"{n:^5} {f(xn):^10.6f} {df(xn):^10.6f} {xn-x0:^10.6f} {(xn-x0)/xn:^10.6f}")
        x0 = xn
        xn = x0 - f(x0) / df(x0)
        n += 1

    print(f"{n:^5} {f(xn):^10.6f} {df(xn):^10.6f} {xn-x0:^10.6f} {(xn-x0)/xn:^10.6f}")

    if n == max_iter:
        print("Iterasi tidak konvergen.")
        return None
    else:
        return xn


def secant(f, x0, x1, tol, max_iter=50):
    print(f"{'n':^5} {'xn':^10} {'f(xn)':^10} {'xn-xn-1':^10}")
    n = 1
    print(f"{n:^5} {x0:^10.6f} {f(x0):^10.6f} {'-':^10}")
    n += 1
    while abs(f(x1)) > tol and n < max_iter:
        xn = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = xn
        print(f"{n:^5} {x0:^10.6f} {f(x0):^10.6f} {x1-x0:^10.6f}")
        n += 1
    if n == max_iter:
        print("Iterasi tidak konvergen.")
        return None
    else:
        return xn


def input_symb(metode="default"):
    x_symbol = sympy.Symbol('x')
    expr = input("Tulis fungsi f(x): ")
    func = sympy.sympify(expr)

    if metode == "newton":
        # Replace the multiplication of `exp()` with the `sympy.exp()` function call.
        func = func.replace(sympy.exp(x_symbol)*sympy.Symbol('*')
                            * sympy.exp(x_symbol), sympy.exp(x_symbol)**2)

    func = sympy.lambdify(x_symbol, func, "numpy")

    def f(x):
        return func(x)

    if metode == "newton":
        diff_func = sympy.diff(expr, x_symbol)
        diff_func_str = sympy.srepr(diff_func).replace('**', '^')
        diff_func_result = sympy.parse_expr(diff_func_str)
        df = sympy.lambdify(x_symbol, diff_func_result, "numpy")
        print(f"Turunan fungsi: df(x) = {diff_func_result}")
        return f, df
    else:
        return f


def f_to_g(f, x):
    # Lakukan transformasi persamaan f(x) menjadi g(x)
    g = sympy.solve(sympy.Eq(f(x), 0), x)[0]
    return g


def input_param(type="bisection"):
    """ Input fungsi secara manual
    def f(x):
        # return x**6-x-1  # Secant: 2, 1, 0.00001
        # return x**3+x-3  # Newton-Rhapson: 1.1, 0.00001
        # return 3/(x-2)  # Iterasi: 4, 0.00001
        # return 5*x**5-3*x**2+x+24  # Regula-Falsi: -1.5, 1, 0.00001
        return math.exp(-x)-x  # Bisection: -1, 1, 0.00001

    def df(x):
        return 3*x**2+1
    """

    if type == "bisection" or type == "regula-falsi":
        f = input_symb()
        a = float(input("Masukkan batas bawah (a): "))
        b = float(input("Masukkan batas atas (b): "))
        tol = float(input("Masukkan nilai toleransi (tol): "))
        return f, a, b, tol
    elif type == "iterasi":
        g = input_symb("iterasi")
        x0 = float(input("Tebakan awal (x0): "))
        tol = float(input("Masukkan nilai toleransi (tol): "))
        return g, x0, tol
    elif type == "newton":
        f, df = input_symb("newton")
        x0 = float(input("Tebakan awal (x0): "))
        tol = float(input("Masukkan nilai toleransi (tol): "))
        return f, df, x0, tol
    elif type == "secant":
        f = input_symb()
        x0 = float(input("Masukkan batas atas (x0): "))
        x1 = float(input("Masukkan batas bawah (x1): "))
        tol = float(input("Masukkan nilai toleransi (tol): "))
        return f, x0, x1, tol


def print_hasil(akar):
    if akar is not None:
        print(f"Akar ditemukan pada x = {akar:.6f}")
    else:
        print("Akar tidak ditemukan.")


def main():
    while True:  # Amankan input loop
        print("=" * 50)
        print(f"{' Program UTS Metode Numerik ':-^50}")
        print("=" * 50)
        print("Metode apa yang ingin digunakan sebagai kalkulasi?")
        print("1. Metode Bisection")
        print("2. Metode Regula-Falsi")
        print("3. Metode Iterasi Titik Tetap")
        print("4. Metode Newton Rhapson")
        print("5. Metode Secant")
        try:
            answer = int(input(">>> Pilihan: "))
            if answer == 1:
                print(f"{' Metode Bisection ':=^50}")
                f, a, b, tol = input_param()
                akar = bisection(f, a, b, tol)
                print_hasil(akar)
            elif answer == 2:
                print(f"{' Metode Regula-Falsi ':=^50}")
                f, a, b, tol = input_param()
                akar = regula_falsi(f, a, b, tol)
                print_hasil(akar)
            elif answer == 3:
                print(f"{' Metode Iterasi Titik Tetap ':=^50}")
                f, x0, tol = input_param("iterasi")
                akar = iterasi_titik_tetap(f, x0, tol)
                print_hasil(akar)
            elif answer == 4:
                print(f"{' Metode Newton Rhapson ':=^50}")
                f, df, x0, tol = input_param("newton")
                akar = newton_rhapson(f, df, x0, tol)
                print_hasil(akar)
            elif answer == 5:
                print(f"{' Metode Secant ':=^50}")
                f, x0, x1, tol = input_param("secant")
                akar = secant(f, x0, x1, tol)
                print_hasil(akar)
            else:
                print(f"{' Pilih antara 1-5 ':!^50}")
                continue

        except ValueError:
            print(f"{' Pilih dengan angka ':!^50}")
            continue

        print("Apakah ingin melakukan kalkulasi lagi?")
        answer = input(">>> Jawaban (y): ")
        if answer.lower().strip() == "y":
            continue
        break


if __name__ == '__main__':
    main()
