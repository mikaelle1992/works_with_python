# **kwags
def resuldo_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')

if __name__ == '__main__':
    
    poduim = {'primeiro':'Ana',
                'segundo':'Pedro', 'terceiro':'Andre'}
resuldo_f1(**poduim)                

#** aceita um dict               