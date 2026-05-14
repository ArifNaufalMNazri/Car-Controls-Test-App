# Imports
import flet as ft 

# App Structure and UI
def main(page: ft.Page):
  page.title = "Car Test App"
  page.theme_mode = ft.ThemeMode.DARK
  page.height = 500
  page.width = 500
  page.resizable = True
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  
  counterUP = ft.TextField( value = "0", width = 70, bgcolor = ft.Colors.WHITE, color = ft.Colors.BLACK, read_only = True, border_radius = 10)
  counterDOWN = ft.TextField( value = "0", width = 70, bgcolor = ft.Colors.WHITE, color = ft.Colors.BLACK, read_only = True, border_radius = 10)
  counterLEFT = ft.TextField( value = "0", width = 70, bgcolor = ft.Colors.WHITE, color = ft.Colors.BLACK, read_only = True, border_radius = 10)
  counterRIGHT = ft.TextField( value = "0", width = 70, bgcolor = ft.Colors.WHITE, color = ft.Colors.BLACK, read_only = True, border_radius = 10)


  def arrowbutton(button_name, function = 0):
    return ft.IconButton(
      icon = button_name,
      icon_color = ft.Colors.WHITE,
      bgcolor = ft.Colors.RED_400,
      icon_size = 50,
      on_click = function
    )
  
  def addcounter(countername):
    countername.value = str(int(countername.value) + 1)
    page.update()

  def clearAll(e):
    counterUP.value = "0"
    counterDOWN.value = "0"
    counterLEFT.value = "0"
    counterRIGHT.value = "0"
    page.update()

  page.add(
    ft.Column(
     controls = [ft.Row([
        counterUP
      ],
      alignment = "center"),

      ft.Row([
        arrowbutton(ft.Icons.ARROW_UPWARD, lambda e : addcounter(counterUP))
      ], 
      alignment = "center"),

      ft.Row([
        counterLEFT, 
        arrowbutton(ft.Icons.ARROW_LEFT, lambda e : addcounter(counterLEFT)),
        ft.Container(content = ft.ElevatedButton(
          "Clear all",
          style = ft.ButtonStyle(
          bgcolor = ft.Colors.RED_400,
          color = ft.Colors.WHITE,
          ),
          icon = ft.Icons.CLOSE,
          on_click = clearAll,
        
        ),
        width = 100
        ),
        arrowbutton(ft.Icons.ARROW_RIGHT, lambda e : addcounter(counterRIGHT)),
        counterRIGHT
      ], 
      alignment = "center"),

      ft.Row([
        arrowbutton(ft.Icons.ARROW_DOWNWARD,  lambda e : addcounter(counterDOWN))
      ],
      alignment = "center"),

      ft.Row([
        counterDOWN
      ],
      alignment = "center")
      ],
     spacing = 10
    )
  )

# Run app
if __name__ == "__main__":
  ft.app(target = main)