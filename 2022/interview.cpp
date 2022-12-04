#include <cstdint>
#include <cstdio>
#include <iostream>
#include <iterator>
#include <map>
using namespace std;

enum class Connectivity
{ 
  FourWay, 
  EightWay
};

/*I'm breaking this graph problem down into three parts - Traversal, Connection, and Labelling. I will proceed as follows:
  1) To traverse, I will be using a recursive function that labels the image as the function 'visits' each pixel in the image.
   Each node that is visited undergoes a check for connectivity between itself and its neigbor.
    Nodes that are not visited are represented by a 0 or 1 (depending on land or not).
     Nodes that are visited are represented by a three digit id or -1 (if the pixel visited was water).
      If they are connected, it will get the label of the neighbor. If they are not connected, the node visited will get a
       different new label (this implies that an overall variable will track these labels). The recursion base case is when
        a particular pixel has no unvisited neigbors.


    I will create two lists, one is my in progress traversal image and one is the final 



   ,  maintain a list of visited nodes. This list will contain tuples of size 2 which represent pixels visited. This ensures that no pixel is visited twice for efficiency. 
  2) 

*/

//Given the connectivity setting, image, and location of two pixels,this function will output whether a given pixel has local connectivity 
bool determineConnectivity(uint8_t **inImage, int pixel1_x, int pixel1_y, int pixel2_x, int pixel2_y, int pixelsWide, int pixelsHigh, Connectivity connectivity){

    //if one of the two pixels are not land they are not connected
    if(inImage[pixel1_x][pixel1_y] != 1 || inImage[pixel2_x][pixel2_y] != 1){
      return false;
    }

    //if one of the two pixels are outside of the image they are not connected
    if(pixel1_x > pixelsWide-1 || pixel1_y > pixelsHigh-1 || pixel1_x < 0 || pixel1_y < 0){
      return false;
    }
    if(pixel2_x > pixelsWide-1 || pixel2_y > pixelsHigh-1 || pixel2_x < 0 || pixel2_y < 0){
      return false;
    }

    //if pixel1's x is not 1 unit away from pixel2's
    if((pixel2_x != pixel1_x) && (pixel2_x != pixel1_x+1) && (pixel2_x != pixel1_x-1)){
      return false;
    }

    //if pixel1's y is not 1 unit away from pixel2's
    if((pixel2_y != pixel1_y) && (pixel2_y != pixel1_y+1) && (pixel2_y != pixel1_y-1)){
      return false;
    }

    //if 4-way connectivity is enabled, then we disallow pixels that are both 1 away x wise and y wise
    if(connectivity == Connectivity::FourWay){
      //if the diff is 1 x wise and y wise, then false
      if(abs(pixel1_x - pixel2_x) == 1 && abs(pixel1_y - pixel2_y) == 1){
        return false;
      }
    }
    //in the 8-way case, we allow pixels that are both 1 away x and y wise which is already included in the above checks so return
    //if we have passed all checks in either case we are connected
    return true;
}

void getIslandsConnected(const uint8_t *inImage, int pixelsWide, int pixelsHigh, Connectivity connectivity,int curr_x,int curr_y, uint8_t **outLabels, std::map<uint8_t, size_t> &outSizes){
  //base case: no surrounding pixels are traversable
  //up
  //if the current pixel is outside of the image 
  if(curr_x > pixelsWide-1 || curr_y > pixelsHigh-1 || curr_x < 0 || curr_y < 0){
    return;
  }
  //base case if the current pixel is visited
  if(inImage[curr_x][curr_y] == -1 || inImage[curr_x][curr_y] != 0 || inImage[curr_x][curr_y] != 1 ){
    return;
  }

  //lets try to traverse the neighors
  //set pixel to visited, even if it is a null node
  if(inImage[curr_x][curr_y] == 0){
    outLabels[curr_x][curr_y] = -1;
  }

  //use the determineConnectivity function to do this

  //if determine connectivity is true
  if(determineConnectivity(inImage, curr_x, curr_y,  curr_x+1, curr_x+1, pixelsWide, pixelsHigh, connectivity)){
    //LABELLING STEP

    
  }
  return 

}


// The requested outputs are encoded as follows: 
// outLabels - label image containing an island identifier per pixel (or 0 if the pixel doesn't belong to that island)
// outSizes  - A map from island ID to size in pixels. The total number of islands is the number of keys in this map 
void findNumberOfIslands(const uint8_t *inImage, int pixelsWide, int pixelsHigh, Connectivity connectivity, 
                         uint8_t **outLabels, std::map<uint8_t, size_t> &outSizes)
{
  //map<int, int> outSizes;





}

// To execute C++, please define "int main()"
int main() {
  
  
  uint8_t image[10][10] = {{1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
                           {1, 1, 0, 0, 0, 1, 0, 0, 0, 0},
                           {1, 0, 0, 0, 0, 1, 0, 0, 0, 0},
                           {0, 0, 0, 0, 0, 1, 1, 0, 0, 0},
                           {0, 0, 0, 0, 1, 0, 0, 1, 0, 0},
                           {0, 0, 0, 0, 1, 0, 0, 1, 1, 0}, 
                           {0, 1, 1, 0, 1, 0, 0, 1, 1, 0}, 
                           {0, 1, 1, 0, 0, 0, 0, 1, 0, 0}, 
                           {0, 1, 1, 1, 0, 0, 0, 0, 0, 0}, 
                           {0, 1, 1, 1, 0, 0, 0, 0, 0, 0}};
  
  /*
  This is an example output for 4-way connectivity
  uint8_t label[10][10] = {{1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
                           {1, 1, 0, 0, 0, 2, 0, 0, 0, 0},
                           {1, 0, 0, 0, 0, 2, 0, 0, 0, 0},
                           {0, 0, 0, 0, 0, 2, 2, 0, 0, 0},
                           {0, 0, 0, 0, 3, 0, 0, 4, 0, 0},
                           {0, 0, 0, 0, 3, 0, 0, 4, 4, 0}, 
                           {0, 5, 5, 0, 3, 0, 0, 4, 4, 0}, 
                           {0, 5, 5, 0, 0, 0, 0, 4, 0, 0}, 
                           {0, 5, 5, 5, 0, 0, 0, 0, 0, 0}, 
                           {0, 5, 5, 5, 0, 0, 0, 0, 0, 0}};
  
  */
  
  // Execute your code here and print the number of islands in the image
  // Add any test cases you see fit

  return 0;
}



