#  cat-generator
<strong><i>a site that generates cats</i></strong> 


# reminders:
- the `index.html` file ***MUST*** stay in the `templates` folder or it will not work 
- this site uses [`flask`](https://pypi.org/project/Flask/) for its API support 
- API thats used: https://some-random-api.ml/animal/cat

ok thats all you need to know, enjoy





<!DOCTYPE html>
<html>
<head>
<title>TR ASH's cat generator</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  
  body{
    background-color:rgb(239, 191, 245);
     }

  h1{
                color:rgb(255, 245, 254);
                font-family:Verdana, Geneva, Tahoma, sans-serif;

            }

  h4,h6,li,dt{
                color:rgb(253, 253, 253);
                font-family:Verdana, Geneva, Tahoma, sans-serif;

            }

  p{
    color:rgb(253, 253, 253);
  }

            a:link{
                color:  purple;
                background-color: transparent;
                text-decoration: none;
            }

            a:visited{
                color: purple;
                background-color: transparent;
                text-decoration: none;
            }

            a:hover{
                color: rgb(255, 104, 242);
                background-color: transparent;
                text-decoration: underline; 
            }    

           a{
                font-family:Verdana, Geneva, Tahoma, sans-serif;

            }
  
</style>
</head>
  <body>
    <i><h1>Welcome to your cat generator</h1></i>
    <br>
     <center><h4>to generate a new cat, refresh the site</h4></center>
    <center><img src="{{cat}}"  height="600"></center>
    <center><h6>fact: {{fact}}</h6></center>
  </body>
</html>

































![lol-min](https://user-images.githubusercontent.com/90879002/209036523-a7d16dfd-48c4-4888-b949-b900dd1eae39.jpg) 
