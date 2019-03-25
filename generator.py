class Generator:
    def __init__(self, num):
        self._num = self.get_all_self_number(num)

    def g(self, num):
        if num >= 1000:
            generate_num = num//1000 + (num % 1000)//100 + (num % 100)//10 + num % 10 + num
            return generate_num
        elif num >= 100:
            generate_num = num // 100 + (num % 100) // 10 + num % 10 + num
            return generate_num
        elif num >= 10:
            generate_num = num // 10 + num % 10 + num
            return generate_num
        else:
            return num + num

    def get_sum(self, num):
        all_number = 0
        all_number += (num * num + num) // 2
        return all_number

    def get_all_self_number(self, num):
        sum = 0
        all_number = self.get_sum(num)
        print(all_number)
        for k in range(1, num):
            generated_num = self.g(k)
            if generated_num > num:
                break
            print(sum)
        return all_number - sum

    def __str__(self):
        return f'l{self._num}l'
if __name__ == "__main__":
    a = '91'
    b = [A for A in a]
    print(b)
    #print({x + sum([int(a) for a in str(x)]) for x in range(1,5000)})
    #print(sum(set(range(1,5000))-{x + sum([int(a) for a in str(x)]) for x in range(1,5000)}))









    #print(sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))