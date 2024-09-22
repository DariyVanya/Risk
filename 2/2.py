from math import sqrt
from colorama import Fore
# coef
variants = {
    "first" : [[0.6, 8], [0.4, -0.5]],
    "second" : [[0.7, 12], [0.3, -0.5]],
    "create a." : [[0.3, 25], [0.7, -1]]
}

def find_M(variant):
    return variants[variant][0][0] * variants[variant][0][1] + variants[variant][1][0] * variants[variant][1][1]

def find_V(variant, M):
    return (variants[variant][0][1] - M)**2 * variants[variant][0][0]  + (variants[variant][1][1] - M)**2 * variants[variant][0][0]

def find_om(V):
    return sqrt(V)

def find_CV(om, M):
    return om/M

def find_SSV(variant, M):

    return sqrt(variants[variant][1][0] * (variants[variant][1][1] - M) **2)

def find_CSV(ssv, M):
    return ssv/M

def find_p(variant):
    return variants[variant][1][0]

def find_Z(variant):
    return variants[variant][1][0] * variants[variant][1][1]

def main():
    print("-- Оцінка ефективності проектів --")
    a = ['Перша корпорація', 'Друга корпорація', 'Створити асоціацію']
    m = [find_M("first"), find_M("second"), find_M("create a.")]
    print(Fore.CYAN + "-- Значення сподіваної чистої теперішньої вартості --", Fore.WHITE)
    for i in range(0, 3):
        print(a[i] + ":", m[i])
    print("Найбільше значення сподіваної чистої теперішньої вартості -", a[ m.index( max(m) ) ], "-" ,max(m))
    print("Найменше значення сподіваної чистої теперішньої вартості -", a[ m.index( min(m) ) ], "-" ,min(m))
    print()

    print(Fore.CYAN + "-- Обчислимо у якості показника кількісної оцінки ризику дисперсію  --", Fore.WHITE)
    a = ['Перша корпорація', 'Друга корпорація', 'Створити асоціацію']
    v = [find_V("first", m[0]), find_V("second", m[1]), find_V("create a.", m[2])]
    for i in range(0, 3):
        print(a[i] + ":", v[i])
    print("\nCередньоквадратичне відхилення:")
    om = [find_om(v[0]), find_om(v[1]), find_om(v[2])]
    for i in range(0, 3):
        print(a[i] + ":", om[i])
    print("Найбільш ризикованим є -", a[ om.index( max(om) ) ], "-" ,max(om))
    print("Найменш ризикованим є -", a[ om.index( min(om) ) ], "-" ,min(om))
    print()

    print(Fore.CYAN + "-- Обчислимо як показник кількісної оцінки ризику коефіцієнт варіації --", Fore.WHITE)
    a = ['Перша корпорація', 'Друга корпорація', 'Створити асоціацію']
    cv = [find_CV(om[0], m[0]), find_CV(om[1], m[1]), find_CV(om[2], m[2])]
    for i in range(0, 3):
        print(a[i] + ":", cv[i])
    print("Найбільш ризикованим є -", a[ cv.index( max(cv) ) ], "-" ,max(cv))
    print("Найменш ризикованим є -", a[ cv.index( min(cv) ) ], "-" ,min(cv))
    print()

    print(Fore.CYAN + "-- Cеміквадратичне відхилення --", Fore.WHITE)
    a = ['Перша корпорація', 'Друга корпорація', 'Створити асоціацію']
    ssv = [find_SSV('first', m[0]), find_SSV('second', m[1]), find_SSV('create a.', m[2])]
    for i in range(0, 3):
        print(a[i] + ":", ssv[i])
    print( "\nКоефіцієнт семіваріації:")
    csv = [find_CSV(ssv[0], m[0]), find_CSV(ssv[1], m[1]), find_CSV(ssv[1], m[2])]
    for i in range(0, 3):
        print(a[i] + ":", csv[i])

    print("Найбільш ризикованим є -", a[ csv.index( max(csv) ) ], "-" ,max(csv))
    print("Найменш ризикованим є -", a[ csv.index( min(csv) ) ], "-" ,min(csv))
    print()

    print(Fore.CYAN + "-- Обчислимо імовірність небажаної події  --", Fore.WHITE)
    a = ['Перша корпорація', 'Друга корпорація', 'Створити асоціацію']
    p = [find_p('first'), find_p('second'), find_p('create a.')]
    for i in range(0, 3):
        print(a[i] + ":", p[i])
    print("Найбільш ризикованим є -", a[ p.index( max(p) ) ], "-" ,max(p))
    print("Найменш ризикованим є -", a[ p.index( min(p) ) ], "-" ,min(p))
    print()

    print(Fore.CYAN + "-- Обчислимо величину сподіваних збитків  --", Fore.WHITE)
    a = ['Перша корпорація', 'Друга корпорація', 'Створити асоціацію']
    z = [find_Z('first'), find_Z('second'), find_Z('create a.')]
    for i in range(0, 3):
        print(a[i] + ":", z[i])
    print("Найбільші збитки має -", a[ z.index( max(z) ) ], "-" ,max(z))
    print("Найменші збитки має -", a[ z.index( min(z) ) ], "-" ,min(z))
    print()
main()