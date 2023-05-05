imgDilate= np.zeros((m,n), dtype=np.uint8)
# SED= np.array([[0,1,0], [1,1,1],[0,1,0]])
# constant1=1

# #Dilation
# for i in range(constant1, m-constant1):
#   for j in range(constant1,n-constant1):
#     temp= img1[i-constant1:i+constant1+1, j-constant1:j+constant1+1]
#     product= temp*SED
#     imgDilate[i,j]= np.max(product)