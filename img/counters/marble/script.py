import os

str = """<div data-category="red" class="red element">
  <div class="filter_img">
      <div class="wrapped_img portfolio_item">
          <img src="img/counters/marble/preview/%s" alt="" width="570" height="570">
          <div class="portf_shape"></div>
          <div class="portfolio_descr">
              <div class="portfolio_title"><h6><a href="portfolio_post1.html">%s</a></h6></div>
              <!-- <div class="portfolio_text">Quisque ut nisl et neque blandit quistum.</div> -->
              <div class="portfolio_btns">
                  <a href="img/counters/marble/%s" class="prettyPhoto zoom_ico" rel="prettyPhoto[portfolio1]">zoom</a>
                  <a href="portfolio_post1.html" class="link_ico">link</a>
              </div>
          </div>
      </div>
  </div>
</div><!-- .element -->
"""

for file in os.listdir("."):
    if file.endswith(".jpg"):
        name = os.path.splitext(file)[0]
        print str % (file, name, file)

# print str
