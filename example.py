# Setup the FOPPL-compiler and auto-importer:
from foppl import Options, imports
# Print additional information:
Options.debug = True

# Import and compile the model:
#import brooks_model_1 as foppl_model
import if_model as foppl_model

# Print out the entire model:
print(foppl_model.model)

# A sample run with the model:
print("=" * 30)
state = foppl_model.model.gen_prior_samples()
pdf = foppl_model.model.gen_pdf(state)
print("Result: {}\nPDF: {}".format(state.get('result', '?'), pdf))

print("=" * 30)
print(foppl_model.model.gen_pdf_code())

print("=" * 30)

for key in sorted(state.keys()):
    print("{}  -> {}".format(key, state[key]))

foppl_model.model.display_graph()