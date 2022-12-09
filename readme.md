# README.MD

## Current Status

- Lỗi phần code nhận diện

## Error Logs

```txt
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 06, 2022 - 09:28:41
Django version 4.0.6, using settings 'demo.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Got the recognize route.
()
Error: OpenCV(4.5.5) :-1: error: (-5:Bad argument) in function 'imwrite'
> Overload resolution failed:
>  - img data type = 17 is not supported
>  - Expected Ptr<cv::UMat> for argument 'img'

[06/Dec/2022 09:28:51] "POST /leafrecog HTTP/1.1" 200 2
```
