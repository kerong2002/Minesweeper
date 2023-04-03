# Minesweeper
### Programer：KeRong&nbsp;&nbsp;Sponsor：KaiHan&nbsp;&nbsp;Used：Python Tkinter &nbsp;&nbsp;Update：2022/09/05

![](https://i.imgur.com/dwHgLaU.png)
- Game_test：https://youtu.be/F9pDrUDzaDE  
- My minesweeper NF best Record：[3.278s](https://youtube.com/shorts/YmPbXsQH2tk)  (2022/06/17)

| Feature | Description |
| --- | --- |
| Cheat mode | Pressing Ctrl + Shift + Alt + up will reveal all bomb locations for easier debugging. |
| Help mode | Pressing Ctrl + h will place a flag, allowing players to mark potential bomb locations for later reference. |
| Restart game | Pressing F2 will start a new game. |
| Difficulty levels | Pressing F3, F4, or F5 will set the difficulty level to easy, medium, or hard, respectively. |
| Exit game | Pressing Ctrl + z will exit the game. |
| No Flag mode | This checkbox option disables the use of flags. |
| Number colors | The numbers on the board are color-coded for better visibility. |
| Refresh game | Clicking the smiley face icon will refresh the game board. |
| Mouse cursor | The cursor changes over the smiley face icon to indicate different game states. |
| Difficulty selection | The menu allows players to choose between easy, medium, hard, and custom difficulty levels. |
| Custom difficulty | Players can customize the game board size and number of bombs using a dropdown menu. |
| Mouse actions | Players can use left, right, and middle mouse clicks to clear tiles and place flags. |
| Auto-expand tiles | When a numbered tile has the correct number of adjacent flags, all surrounding tiles will automatically be cleared. |
| Scary face | The smiley face icon turns into a scared face when the player clicks on a bomb tile. |
| Flag placement error | If a flag is placed incorrectly, an X will appear on the board and the game is lost. |


遊玩方式：  
以所選取該點，開始掃雷，場上數字是以它為中心的九宮格，標示炸彈的數量。    
例：  
```py
💣 💣 2
💣 4  2
1   2 💣
```
數字4周圍的九宮格含有四顆炸彈，所以中間標示數字為4  
**目標**: 不要踩到任何炸彈，除去非炸彈的位置，即可獲得勝利  
          不插旗幟，點完全圖非炸彈位置，也視為勝利     

 
## 2022/04/21 v1.0   
功能補齊:  
1.滑鼠左鍵開啟該方塊  
2.滑鼠右鍵插下旗幟(第二次取消插旗)  
3.menu菜單(可刷新new game和離開)  
4.笑臉可以刷新  
5.踩地雷贏了會變臉  
6.踩到炸彈會哭臉  
7.踩到的那顆炸彈會顯示不同顏色  
8.插錯旗幟(插到不是炸彈的位置)會打X  
 
## 2022/04/22 v1.0 update
功能補齊:  
1.滑鼠中鍵特殊擴散(前替是點擊該點數字周圍有相對應數量的旗幟數)   
2.時間不會有停止計算狀況  
3.炸彈數量除錯  
4.贏了會自動插旗幟且炸彈數量會顯示0  
 
## 2022/04/23 v1.0 update 
功能補齊:  
1.數字顏色  
2.旗幟顏色    
3.字體大小和位置調整  
4.場地顏色  
5.按鈕浮起  
6.笑臉按鈕調整位置  
7.menu菜單的help更新  
8.按鈕大小調整  
 
## 2022/04/23 v2.0    
功能調整:  
1.新增滑鼠游標會在笑臉上有不同圖標  
2.提供關卡難度選擇  
3.easy模式為9*9的大小(10顆地雷)  
4.normal模式16*16的大小(40顆地雷)  
5.更正easy的視窗大小  
6.更正整個視窗的按鈕安排與大小  
7.除去舊有的Button and Label  
 
## 202/04/24 v3.0  
功能改進:  
1.三種難度選擇  
2.新增hard模式，30*16的大小(99顆炸彈)  
3.炸彈、笑臉和計時位置修改  
4.視窗大小調整  
5.重新制定按鈕大小  
6.menu字體調整  
發現問題:  
1.建置場地的速度過慢(演算法耗時)  (尚未修正)  
2.左右建尚未建置功能   (已改善)
 
## 2022/04/24 v3.1   
小功能改進:   
1.炸彈bug測試  
2.模式菜單改進  
 
## 2022/04/24 v3.2     
小功能改進:  
1.配置數字作些許調整    
2.左右鍵功能加入  
3.修改做鍵鍵觸發規則  
 
## 2022/04/24 v3.3     
功能改進:    
1.按鈕位置加上外框   
2.建置和刷新button調整寫法(加速)  
3.新設定按鈕調為跟外框做調整，填滿整個外框  
4.調整視窗大小  
5.smile和Label位置調整  
6.左右鍵功能bug修復  
 
## 2022/04/24 v4.0    
功能更新:    
1.按鈕調整為固定位置  
2.上方的炸彈數，計時，和笑臉也會隨著場地大小而更動位置  
3.綁定炸彈數必定靠左  
4.綁定計時必定靠右  
5.綁定笑臉必定至中隊齊  
6.按鈕操作改善優化  
7.新增可自訂義寬按鈕數、高按鈕數和炸彈數功能  
8.自訂義跟模式選擇都會自動改變視窗大小  
9.防止玩家在自訂義輸入任意數導致爆炸，限制使用者輸入上限和下限  
10.字體調整SIZE  
11.menu新增遊玩說明  
 
## 2022/04/25 v4.1     
功能改進:  
1.視窗優化    
2.視窗會隨著大小有規律變化  
3.Label和笑臉位置優化  
4.程式碼優化執行速度    
 
## 2022/04/25 v4.2      
功能改進:  
1.視窗位置自動調整  
2.視窗大小再次改進  
3.custom字體和位置調整   
4.custom 寬高限制調整  
5.加入快捷鍵F2刷新遊戲  
6.加入快捷鍵ctrl+z離開遊戲  
7.重新定義三種基本模式的視窗位置和大小  
 
## 2022/04/25 v4.3          
功能改進:    
1.左鍵點下去還未放開始，會是oops臉    
2.difficult三種難度快捷鍵加入    
3.新增No_Flag(FA)模式  
4.新增Author  
5.新增help功能  
6.help功能綁快捷鍵  
 
## 2022/04/25 v4.4          
功能改進:  
1.炸彈數量原本會因為擴散而沒有變動  
2.NF模式的笑臉會不一樣  
3.Ctrl+H 幫助模式修復bug  
 
## 2022/04/29 v4.41          
bug改進:   
1.空白磚塊bug  
 
## 2022/04/30 v4.42         
bug改進:   
1.空白磚塊bug  

## 2022/06/19 v5.0   
1.新增點下數字，周圍會凹陷，幫助玩家偵測  
