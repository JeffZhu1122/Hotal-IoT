<!DOCTYPE>
<html lang="zh-cn">

<head>
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
     <title>ADMIN EVENTS</title>
     <style>
          .sortable-ghost {
               opacity: 0.4;
               background-color: #F4E2C9;
          }

          .block__list li {
               cursor: pointer;

          }
     </style>
</head>
<!--      <link href="app.css" rel="stylesheet" type="text/css"/>
      -->
<!-- script src="./Sortable.js"></script> -->
<script src="https://cdn.bootcss.com/Sortable/1.8.3/Sortable.js"></script>

<body>
        <p><h2>Events</h2></p>

        <form action="/admin" method="post">
            <br>
            % for i in range(0,len(time)):
            {{name[i]}}: <input type="text" name="{{name[i]}}" value="{{time[i]}}" />
            
            <ul id="foo{{i}}" class="block__list block__list_words">
                Actions:
                <br>
                % for j in range (0,len(action[i])):
                {{j+1}}. {{list(action[i][j].keys())[0]}}: {{list(action[i][j].values())[0]}}
                <br>
                % end
            </ul>
            <br>
            % end
            <br>
            <input value="submit" type="submit" />
        </form>
     <script>
        % for i in range(0,len(time)):
        Sortable.create(document.getElementById('foo{{i}}'), {
            animation: 150,
            onAdd: function (evt) {
                console.log('onAdd.foo:', [evt.item, evt.from]);
            },
            onUpdate: function (evt) {
                console.log('onUpdate.foo:', [evt.item, evt.from]);
            },
            onRemove: function (evt) {
                console.log('onRemove.foo:', [evt.item, evt.from]);
            },
            onStart: function (evt) {
                console.log('onStart.foo:', [evt.item, evt.from]);
            },
            onSort: function (evt) {
                console.log('onSort.foo:', [evt.item, evt.from]);
            },
            onEnd: function (evt) {
                console.log('onEnd.foo:', [evt.item, evt.from]);
            }
        });
        % end
     </script>
</body>

</html>