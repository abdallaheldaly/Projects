<!-- This is a task I took from a company, this code as the company gave it to me. -->


<!-- <?php
/**
Implement a groupByManager function that:

Accepts an associative array containing the manager name for each employee.
Returns an associative array containing an array of employees for each manager , in any order.
For example, for associative array ["Mohamed" => "Yasser", "Ramadan" => "Yasser", "Amr" => "Nasr"] the groupByOwners function should return ["Yasser" => ["Ramadan", "Mohamed"], "Nasr" => ["Amr"]].
**/
function groupByOwners($data){
    //write your code here
    $newData=array();
    foreach($data as $manager => $employee) {
        //echo "[" . $employee . " => " . $manager . "]";
        $stored_employee = $employee;

    }
    
}

//don't edit after this line
$data=array ("Mohamed" => "Yasser", "Ramadan" => "Yasser", "Amr" => "Nasr","Saeed" => "Yasser","Aly" => "Mohamed");
$resultArray= groupByOwners($data);


echo '<pre>';
print_r($data);//print the result associative array with the files name group by owner
echo '</pre>';

?> -->




<!-- /////////////////////////Solution////////////////////////-->




<?php
/**
 * Implement a groupByManager function that:
 * Accepts an associative array containing the manager name for each employee.
 * Returns an associative array containing an array of employees for each manager, in any order.
 * 
 * Example: 
 * For associative array ["Mohamed" => "Yasser", "Ramadan" => "Yasser", "Amr" => "Nasr"] 
 * the groupByOwners function should return ["Yasser" => ["Ramadan", "Mohamed"], "Nasr" => ["Amr"]].
 */

function groupByOwners($data) {
    return array_reduce($data, function($carry, $employeeManager) {
        list($employee, $manager) = $employeeManager; // Extract employee and manager from the array
        // If the manager is not in the result, add them with an empty array
        if (!isset($carry[$manager])) {
            $carry[$manager] = [];
        }
        // Add the employee to the list of employees under the same manager
        $carry[$manager][] = $employee;
        return $carry;
    }, []); // Initialize with an empty array
}

// Test the function with the provided data
$data = array("Mohamed" => "Yasser", "Ramadan" => "Yasser", "Amr" => "Nasr", "Saeed" => "Yasser", "Aly" => "Mohamed");
$resultArray = groupByOwners($data);

echo '<pre>';
print_r($resultArray); // Print the grouped result
echo '</pre>';
?>




<!-- /////////////////////////Solution////////////////////////// -->



<!-- <?php
/**
 * Implement a groupByManager function that:
 * Accepts an associative array containing the manager name for each employee.
 * Returns an associative array containing an array of employees for each manager, in any order.
 * 
 * Example: 
 * For associative array ["Mohamed" => "Yasser", "Ramadan" => "Yasser", "Amr" => "Nasr"] 
 * the groupByOwners function should return ["Yasser" => ["Ramadan", "Mohamed"], "Nasr" => ["Amr"]].
 */

function groupByOwners($data) {
    $newData = array();
    
    // Iterate through the input data array
    foreach ($data as $employee => $manager) {
        // If the manager is not in the newData array, add them with an empty array
        if (!isset($newData[$manager])) {
            $newData[$manager] = array();
        }
        
        // Append the employee under the appropriate manager
        $newData[$manager][] = $employee;
    }
    
    return $newData; // Return the grouped associative array
}

// Test the function with the provided data
$data = array("Mohamed" => "Yasser", "Ramadan" => "Yasser", "Amr" => "Nasr", "Saeed" => "Yasser", "Aly" => "Mohamed");
$resultArray = groupByOwners($data);

echo '<pre>';
print_r($resultArray); // Print the grouped result
echo '</pre>';
?> -->

