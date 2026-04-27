from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_leaf_visualiser import page_leaf_visualiser_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_body


app = MultiPage(app_name="Mildew Detection in Cherry Leaves")

app.add_page("Project Summary", page_summary_body)
app.add_page("Leaf Visualiser", page_leaf_visualiser_body)
app.add_page("Mildew Detector", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance", page_ml_performance_body)

app.run()