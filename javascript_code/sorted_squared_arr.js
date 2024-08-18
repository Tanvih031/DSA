function sortedSquaredArray(array){
    //write code here.make sure to return desired array 
    let squared_arr = []
    for(let i=0;i<array.length;i++){
        squared_arr.push(array[i] * array[i])
    }
    let sorted_array = squared_arr.sort((a, b) => a - b)
    return sorted_array

}
console.log(sortedSquaredArray([-4, -2, 0, 1, 2]));