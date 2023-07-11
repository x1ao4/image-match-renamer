# image-match-renamer
使用 image-match-renamer 可以将图片文件名与文本数据进行匹配，并按照匹配的数据批量重命名图片文件。

## 功能演示
假设您有一个名为 `data.txt` 的文本文件，其中包含一些电视剧集的信息。

`data.txt` 的内容如下：
```
1;2023-01-01;45;The first episode
2;2023-01-08;45;The second episode
3;2023-01-15;45;The third episode
```
您还有一些图像文件，文件名中包含电视剧集的标题。例如：
```
2023-01-01 The first episode.jpg
2023-01-08 The second episode.jpg
2023-01-15 The third episode.jpg
```
您希望根据文本文件中的数据，将图像文件重命名为对应的剧集编号。

运行 `image-match-renamer.py` 脚本后，脚本会自动查找与文本文件中标题匹配的图像文件，并将它们重命名为对应的剧集编号。例如：
```
2023-01-01 The first episode.jpg > 1.jpg
2023-01-08 The second episode.jpg > 2.jpg
2023-01-15 The third episode.jpg > 3.jpg
```

## 运行条件
- 请确保您的系统上安装了 Python 3.0 或更高版本。

## 注意事项
- 请确保数据文件 `data.txt` 的格式与脚本中所述的格式一致，即每一行都包含四个由分号分隔的字段，分别表示剧集编号、日期、时长和标题。
- 图像文件名的格式应符合脚本中的命名规则，需要包含剧集标题，并以 `.jpg` 作为文件扩展名。
- 在运行脚本之前，请备份原始的数据文件和图像文件，以防数据丢失或重命名错误。

## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改 `start.command (Mac)` 或 `start.bat (Win)` 中的路径，以指向您存放 `image-match-renamer.py` 脚本的目录。
3. 在脚本中指定文本文件和图像文件所在的目录。
4. 双击运行 `start.command` 或 `start.bat` 脚本以执行 `image-match-renamer.py` 脚本。
5. 脚本会自动查找与文本文件中标题匹配的图像文件，并将它们重命名为对应的剧集编号。
<br>

# line-indexer
With image-match-renamer, you can match image filenames with text data and batch rename image files according to the matched data.

## Demo
Suppose you have a text file named `data.txt` that contains information about some TV episodes.

The content of `data.txt` is as follows:
```
1;2023-01-01;45;The first episode
2;2023-01-08;45;The second episode
3;2023-01-15;45;The third episode
```
You also have some image files with filenames that contain the title of the TV series. For example:
```
2023-01-01 The first episode.jpg
2023-01-08 The second episode.jpg
2023-01-15 The third episode.jpg
```
You want to rename the image files to their corresponding episode numbers based on the data in the text file.

After running the `image-match-renamer.py` script, the script will automatically find image files that match the title in the text file and rename them to their corresponding episode numbers. For example:
```
2023-01-01 The first episode.jpg > 1.jpg
2023-01-08 The second episode.jpg > 2.jpg
2023-01-15 The third episode.jpg > 3.jpg
```

## Requirements
- Make sure Python 3.0 or higher is installed on your system.

## Notes
- Make sure that the format of the data file `data.txt` is consistent with the format described in the script, i.e., each line contains four fields separated by semicolons, representing the episode number, date, duration, and title.
- The format of the image filename should conform to the naming rules in the script, which should include the title of the episode and use `.jpg` as the file extension.
- Before running the script, please back up your original data and image files to prevent data loss or renaming errors.

## Usage
1. Clone or download the repository to a directory on your computer.
2. Modify the path in `start.command (Mac)` or `start.bat (Win)` to point to the directory where you store the `image-match-renamer.py` script.
3. Specify the directory where the text file and image files are located in the script.
4. Double-click `start.command` or `start.bat` to execute the doc-merger.py script.
5. The script will automatically find image files that match the title in the text file and rename them to their corresponding episode numbers.
