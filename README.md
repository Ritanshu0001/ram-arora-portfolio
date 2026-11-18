# Ram Arora Portfolio

A responsive static portfolio focused on finance, operations and supply chain interests, prepared for ramarora09.com.

Includes a professional portrait, biography, education, research and academic projects, seven certificate previews, contact links and an updated one-page resume. The resume includes Project CONNECT and the latest LinkedIn Learning certificates; HR Professional App Design has been removed from the portfolio and CV.

## Run or deploy

Serve this folder with any static web server. No site build or dependencies are required.

For GitHub Pages, select the main branch and repository root in the Pages settings. The CNAME file contains ramarora09.com; configure your domain DNS for your chosen hosting provider.

## Edit

- index.html: content and links
- styles.css: template styles
- ram.css: portfolio-specific responsive styles
- script.js: navigation and animated background
- certificates.js: certificate filters and viewer
- assets/: images and previews
- documents/: resume, reports, presentation and certificates
- scripts/build_resume.py: editable resume content and PDF generator

## Update the resume

Install Python's reportlab package, then run `python3 scripts/build_resume.py` to regenerate documents/Ram_Arora_Resume.pdf. Refresh assets/resume-preview.png with Poppler after changing the PDF.
