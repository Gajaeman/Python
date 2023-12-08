product={'비누':[3,2],'칫솔':[5,4],'샴푸':[2,1],'치약':[4,4],'로션':[5,3]}
good=[]
bad=[]
for product_name,[sale,customer] in product.items():
    if(sale>=4) and (customer>=4) :
        good.append(product_name)
    elif(sale<=4) and (customer<4):
        bad.append(product_name)

print('우수제품은', good)
if '로션' in bad:
    print('로션은 판매중지에 해당됨')
else:
    print('로션은 판매중지에 해당 안 됨')
