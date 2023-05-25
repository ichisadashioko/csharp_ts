using System;
using System.Windows.Forms;

public class Program {
  public static void copy_text_to_clipboard(string text) {
    try {
      Clipboard.SetText(text);
    } catch (Exception ex) {
      Console.WriteLine(ex);
      Console.WriteLine(ex.Message);
    }
  }

  [STAThread]
  public static void Main() {
    long unix_ts = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
    string ts_s = unix_ts.ToString();
    Console.WriteLine(ts_s);
    copy_text_to_clipboard(ts_s);
  }
}
