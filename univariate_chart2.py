fig = (px.histogram(lol_data,
                    x="kills",
                    facet_col= "position",
                    facet_row = "result",
                    title="Kills Distribution Per Position",
                    histnorm="probability density")
      )
fig.show()

fig.write_html("plot2.html")
