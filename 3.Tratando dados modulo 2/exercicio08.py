Medida = float(input("Digite uma distancia em metros: "))

km = Medida /1000
hm = Medida /100
dam = Medida * 10
cm = Medida * 100
mm = Medida * 1000

print("A medida de %.1f corresponde a \n %.3f km \n %.2f hm \n  %.2f dam \n  %.2f cm \n  %.2f mm \n " %(Medida,km, hm, dam, cm, mm))