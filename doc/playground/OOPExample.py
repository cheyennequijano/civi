## Java class/intialization
#  class Stockpile {
#     private int myFood;
## only necessary to specify the type

#     public Stockpile() {
#         myFood = 0;
#     }
# }

class Stockpile:

    def __init__(self):
        self.food = 0

    def add_food(self, amount):
        self.food += amount
        

class GameWorld:

    def update(self):
        for villager in self.villagers:
            villager.update_self(self.stockpile)

# public interface Task {
#     public void execute(Stockpile stockpile);
# }

# public class GatheringTask implements Task {
#     public void execute(Stockpile stockpile) {
#       stockpile.addRawFood(1);
#     }
# }

# public class CookingTask implements Task {
#     public void execute(Stockpile stockpile) {
#       stockpile.removeRawFood(1);
#       stockpile.addCookedFood(1);
#     }
# }

# new ArrayList<Integer>(); // 😀
# new List<Integer>(); // SYNTAX ERROR

# public interface List<T> {
#   public void add(T t);
#   public T get(int index);
# }

# public class ArrayList<T> implements List<T> {
#   private T[] myArray;
#   private int myLength;
#
#   public void add(T t) {
#       myArray[myLength] = t;
#       myLength += 1;
#   }
# 
#   public T get(int index) {
#        ...gets something from the list
#   }
# }
#
# public void main() {
#   ArrayList<Integer> a = new ArrayList<>();
#   ArrayList<Integer> b = new ArrayList<>();
#   a.add(5);
#   b.add(7);
#   a.add(7); // a has myLength = 2, b has myLength = 1
# }

# It's an interface!
class Task:

    def execute(self, stockpile):
        pass



class Villager:

    def __init__(self, initial_task):
        self.current_task = initial_task

    def assign_task(self, new_task):
        self.current_task = new_task

    def update_self(self, stockpile):
        self.hunger -= 1
        self.current_task.execute(stockpile)
        # BOO
        #  if gathering, add to food stockpile
        # if self.task == 'gathering':
        #     stockpile.add_food(1)
        # elif self.task == 'mining':
        #     stockpile.add_stone(1)
        # elif self.task == 'woodcutting':
        #     stockpile.add_wood(1)



if __name__=='__main__':
    # once every 0.167 seconds, call GameWorld.update
