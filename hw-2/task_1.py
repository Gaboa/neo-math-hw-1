import matplotlib.pyplot as plt
from matplotlib_venn import venn3

rock_fans = {101, 102, 103, 105, 107, 109, 110, 112, 115, 118}
pop_fans = {102, 104, 105, 106, 108, 110, 111, 113, 115, 117}
jazz_fans = {103, 105, 108, 110, 112, 114, 115, 116, 119, 120}

# Unique fans
unique_fans = rock_fans | pop_fans | jazz_fans

# Fans who like all three genres
all_genre_fans = rock_fans & pop_fans & jazz_fans

# Only rock fans
unique_rock_fans = rock_fans - pop_fans - jazz_fans

# Two genre fans
rock_pop_fans = (rock_fans & pop_fans) - jazz_fans
rock_jazz_fans = (rock_fans & jazz_fans) - pop_fans
pop_jazz_fans = (pop_fans & jazz_fans) - rock_fans
two_genre_fans = rock_pop_fans | rock_jazz_fans | pop_jazz_fans


print("Unique fans:", unique_fans)
print("All genre fans:", all_genre_fans)
print("Unique rock fans:", unique_rock_fans)
print("Two genre fans:", two_genre_fans)

# Venn diagram
venn3((rock_fans, pop_fans, jazz_fans), ('Rock', 'Pop', 'Jazz'))
plt.show()