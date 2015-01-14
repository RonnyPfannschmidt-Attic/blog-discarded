what happens when porting c to vala
===================================

:date: 2008-08-18
:tags: pida, gtk, vala


Since the paned widget of <a href="http://pida.co.uk">pida</a> (for the sidebars) is written in c and i have to maintain it,
i started porting it 1:1 to <a href="http://live.gnome.org/Vala">Vala</a>.

The results are stunning in terms of LOC and code readability.

Take this c simple c helper function:
<sourcecode syntax="c">
void
_moo_window_set_icon_from_stock (GtkWindow  *window,
                                 const char *name)
{
    GdkPixbuf *icon;
    GtkStockItem dummy;

    g_return_if_fail (GTK_IS_WINDOW (window));
    g_return_if_fail (name != NULL);

    if (gtk_stock_lookup (name, &dummy))
    {
        icon = gtk_widget_render_icon (GTK_WIDGET (window), name,
                                       GTK_ICON_SIZE_BUTTON, 0);

        if (icon)
        {
            gtk_window_set_icon (GTK_WINDOW (window), icon);
            gdk_pixbuf_unref (icon);
        }
    }
    else
    {
        gtk_window_set_icon_name (GTK_WINDOW (window), name);
    }
}
</sourcecode>


and it looks like this in vala:
<sourcecode syntax="csharp">
void set_icon_from_stock(Window window, string stock_id)
{
    StockItem dummy;
    if(Gtk.stock_lookup(stock_id, dummy))
    {
        var icon = window.render_icon(stock_id, Gtk.IconSize.BUTTON, null);
        window.icon = icon;
    }
    else
    {
        window.icon_name = stock_id;
    }
}
</sourcecode>


But thats only getting started, the ease of signals, properties, data-hiding and is really stunning compared to c.

Vala has all i need for nice enough GUI programming, yet its entirely ABI/API-compatible to gtk+ in c.
Thanks to the vala team, keep up the great work.