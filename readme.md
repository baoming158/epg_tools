## this tool is for batch update epg abs_id and send mq message
mq notice message
```
{
  "id": "5d7aa615-acb1-47fd-b8e1-f97bc66274a8",
  "description": "删除栏目:[44198877]硬骨头 41-信息成功",
  "time": "2018-02-02 00:11:21",
  "data": [
    {
      "id": 44198876,
      "type": 1
    },
    {
      "id": 44198877,
      "type": 2
    }
  ]
}
```

visit method
```
visit url :http://0.0.0.0:5000/api/update_abs this method's file is fixed epg.txt
epg.txt
column_id abs_id
```