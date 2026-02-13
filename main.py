import pandas as pd
import plotly.express as px
import sys

def removeDeadColumns (df):
  droppedColumns= []

  for col in df.columns:
    if "Analog Input" in col and df[col].nuniuque()==1:
      droppedColumns.append(col)

  df= df.drop(columns=droppedColumns)
  
  print(f"Removed dead sensors: {droppedColumns}")
  return df

def graphPlot(df)
  if "RPM" in df.columns:
    fig_rpm= px.line(df, y="RPM", title="RPM Over Time")
    fig_rpm.show()

  if "TPS" in df.columns:
    fig_tps= px.line(df, y="TPS", title="TPS Over Time")
    fig_tps.show()

def main():
  if len(sys.argv) !=2:
    print("Invalid")
    return

  file_path= sys.argv[1]

df= pd.read_csv(file_path)

df = removeDeadColumns(df)

graphPlot(df)

if _name_ == "_main_":
  main()
