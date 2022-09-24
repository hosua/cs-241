m=0
n=10

output_file="le-proof.txt"

# proof by exhaustion lul
file = open(output_file, "w")
for i in range(m,n):
    for j in range(m,n):
        output = ""
        foo = str((i,j)*9)
        x = int(foo.replace(",","").replace(" ", "").replace(")", "").replace("(", ""))
        if x == 0:
            continue
        y = 37
        k = x / y
        # Let $k$ be some number in $37k = 999999999999999999$
        # $k = \frac{9999999999999999}{37} = 27027027027027028$, $k \in \mathbb{Z}$
        # $ \therefore  37|9999999999999999999$ \\
        # print(f"{999999999999999999/37:.0f}")

        output += f"Let $k$ be some number in $37k = {x}$\n\n"
        output += "$k = \\frac{" + str(x) + "}{" + str(y) + "} = "
        output += f"{k:.0f}"
        output += "$, $k \in \mathbb{Z}$\n\n"
        output += f"$ \\therefore  {y}|{x} $ \\\\\n\n"
        file.write(output)
        print(output, end="")

file.close()
