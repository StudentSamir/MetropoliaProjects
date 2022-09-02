kuha=float(input("Anna kuhan pituus senttimetreinä:"))

if kuha<37:
    print("Laske kuha takaisin järveen."+" Kuha on alimittainen "+str(37-kuha)+" senttimetrillä.")
else:
    print("Hieno saalis!")