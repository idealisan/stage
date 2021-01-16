Markdown cells support standard Markdown syntax as well as GitHub Flavored Markdown (GFM). Open the preview to see these rendered.

### Basics

# H1
## H2
### H3
#### H4
##### H5
###### H6

---

*italic*, **bold**, ~~Scratch this.~~

`inline code`

### Lists

1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.

### Quote

> Peace cannot be kept by force; it can only be achieved by understanding.

### Links

[I'm an inline-style link](https://www.google.com)
http://example.com

You can also create a link to another note: (Note menu -> Copy Note Link -> Paste)
[01 - Getting Started](quiver-note-url/D2A1CC36-CC97-4701-A895-EFC98EF47026)

### Tables

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

### GFM Task Lists

- [ ] a task list item
- [ ] list syntax required
- [ ] normal **formatting**, @mentions, #1234 refs
- [ ] incomplete
- [x] completed

### Inline LaTeX

You can use inline LaTeX inside Markdown cells as well, for example, $x^2$.

![图片](sample.assets/image-20210115190603272.png)

# C Sharp 实现图形界面版TCPing

界面设计

![](C#%20%E5%AE%9E%E7%8E%B0%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E7%89%88TCPing.assets/image-20200222180320422-1582366626417.png)

代码

```c#
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using System.Net.Sockets;

namespace TCPing
{
    public partial class Form1 : Form
    {

        private string okText = "连通了";
        private Color okColor = Color.Green;
        private string failText = "连不通";
        private Color failColor = Color.Red;
        private bool status = false;
        private string excMsg = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void ping_Click(object sender, EventArgs e)
        {
            result.ForeColor = Color.Black;
            result.Text = "正在测试...";
            using (BackgroundWorker bw = new BackgroundWorker())
            {
                bw.RunWorkerCompleted += new RunWorkerCompletedEventHandler(changeResilt);
                bw.DoWork += new DoWorkEventHandler(onClickPing);
                bw.RunWorkerAsync();
            }
            ping.Enabled = false;
        }

        private void changeResilt(object sender, RunWorkerCompletedEventArgs e)
        {
            if (status)
            {
                result.ForeColor = okColor;
                result.Text = okText;
            }
            else
            {
                result.ForeColor = failColor;
                result.Text = failText + ":" + excMsg;
            }
            ping.Enabled = true;
        }

        private void onClickPing(object sender, DoWorkEventArgs ev)
        {
            string host = this.hostname.Text;
            int port = Int32.Parse(this.port.Text);
            status = connect(host, port);
        }

        private bool connect(string host, int port)
        {
            bool ret = false;
            try
            {
                TcpClient tcp = new TcpClient(host, port);               
                NetworkStream s = tcp.GetStream();
                bool b = s.CanRead;
                ret = true;
                s.Close();
                tcp.Close();                
            }
            catch (Exception e)
            {
                excMsg = e.Message;
            }

            return ret;
        }
    }
}

```

运行效果测试

![image-20200222180335217](C#%20%E5%AE%9E%E7%8E%B0%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E7%89%88TCPing.assets/image-20200222180335217.png)

![image-20200222180411386](C#%20%E5%AE%9E%E7%8E%B0%E5%9B%BE%E5%BD%A2%E7%95%8C%E9%9D%A2%E7%89%88TCPing.assets/image-20200222180411386.png)

<a href="TCPing.exe" >下载</a>

