// DOM Elements
const analysisForm = document.getElementById('analysisForm');
const submitBtn = document.getElementById('submitBtn');
const resultsSection = document.getElementById('resultsSection');
const errorMessage = document.getElementById('errorMessage');
const tabBtns = document.querySelectorAll('.tab-btn');
const resultsOutputs = {
    analysis: document.getElementById('analysisOutput'),
    profile: document.getElementById('profileOutput'),
    resume: document.getElementById('resumeOutput'),
    refined: document.getElementById('refinedOutput'),
    interview: document.getElementById('interviewOutput')
};

let currentResults = null;

// File input styling
const resumeFile = document.getElementById('resumeFile');
const fileWrapper = document.querySelector('.file-input-wrapper');

resumeFile.addEventListener('change', (e) => {
    const fileName = e.target.files[0]?.name;
    const placeholder = fileWrapper.querySelector('.file-placeholder');
    if (fileName) {
        placeholder.textContent = `📄 ${fileName}`;
        placeholder.style.borderStyle = 'solid';
    }
});

// Drag and drop
fileWrapper.addEventListener('dragover', (e) => {
    e.preventDefault();
    fileWrapper.style.background = '#f0f2ff';
});

fileWrapper.addEventListener('dragleave', () => {
    fileWrapper.style.background = '';
});

fileWrapper.addEventListener('drop', (e) => {
    e.preventDefault();
    fileWrapper.style.background = '';
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        resumeFile.files = files;
        const placeholder = fileWrapper.querySelector('.file-placeholder');
        placeholder.textContent = `📄 ${files[0].name}`;
        placeholder.style.borderStyle = 'solid';
    }
});

// Tab switching
tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        tabBtns.forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
        
        btn.classList.add('active');
        const tabName = btn.dataset.tab;
        document.getElementById(`${tabName}-tab`).classList.add('active');
    });
});

// Form submission
analysisForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const jobUrl = document.getElementById('jobUrl').value;
    const githubUsername = document.getElementById('githubUsername').value;
    const resumeFile = document.getElementById('resumeFile').files[0];
    const provider = document.getElementById('llmProvider')?.value;
    const apiKey = document.getElementById('apiKey')?.value;
    const ollamaModel = document.getElementById('ollamaModel')?.value;

    if (!jobUrl) {
        showError('Please enter a job posting URL');
        return;
    }

    // Prepare form data
    const formData = new FormData();
    formData.append('job_url', jobUrl);
    if (githubUsername) formData.append('github_username', githubUsername);
    if (resumeFile) formData.append('resume_file', resumeFile);
    if (provider) formData.append('provider', provider);
    if (apiKey) formData.append('api_key', apiKey);
    if (ollamaModel) formData.append('ollama_model', ollamaModel);

    // Show loading state
    submitBtn.disabled = true;
    const btnText = submitBtn.querySelector('.btn-text');
    const spinner = submitBtn.querySelector('.spinner');
    btnText.textContent = 'Analyzing...';
    spinner.classList.remove('hidden');
    hideError();

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Analysis failed');
        }

        const result = await response.json();
        
        if (result.status === 'success') {
            displayResults(result.data);
            resultsSection.classList.remove('hidden');
            currentResults = result.data;
            window.scrollTo({ top: resultsSection.offsetTop - 100, behavior: 'smooth' });
        } else {
            throw new Error('Unexpected response format');
        }
    } catch (error) {
        console.error('Error:', error);
        showError(`Error: ${error.message}`);
    } finally {
        submitBtn.disabled = false;
        btnText.textContent = 'Analyze Position';
        spinner.classList.add('hidden');
    }
});

// Display results in tabs
function displayResults(data) {
    resultsOutputs.analysis.textContent = data.analysis || 'No analysis available';
    resultsOutputs.profile.textContent = data.profile_data || 'No profile data available';
    resultsOutputs.resume.textContent = data.resume_draft || 'No resume draft available';
    resultsOutputs.refined.textContent = data.refined_output || 'No refined output available';
    resultsOutputs.interview.textContent = data.interview_prep || 'No interview prep available';
}

// Copy to clipboard
function copyToClipboard(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    
    navigator.clipboard.writeText(text).then(() => {
        const btn = event.target;
        const originalText = btn.textContent;
        btn.textContent = '✓ Copied!';
        setTimeout(() => {
            btn.textContent = originalText;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
        showError('Failed to copy to clipboard');
    });
}

// Download results as text file
function downloadResults() {
    if (!currentResults) return;

    const content = `
=== CAREER ASSISTANT ANALYSIS RESULTS ===

--- JOB ANALYSIS ---
${currentResults.analysis}

--- PROFILE DATA ---
${currentResults.profile_data}

--- RESUME DRAFT ---
${currentResults.resume_draft}

--- REFINED RESUME ---
${currentResults.refined_output}

--- INTERVIEW PREPARATION ---
${currentResults.interview_prep}
    `.trim();

    const blob = new Blob([content], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `career-analysis-${new Date().toISOString().split('T')[0]}.txt`;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
}

// Reset form
function resetForm() {
    analysisForm.reset();
    resultsSection.classList.add('hidden');
    currentResults = null;
    
    // Reset file placeholder
    const placeholder = document.querySelector('.file-placeholder');
    placeholder.textContent = 'Choose a file or drag and drop';
    placeholder.style.borderStyle = 'dashed';
}

// Error handling
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
}

function hideError() {
    errorMessage.classList.add('hidden');
}

// Initialize
console.log('Career Assistant UI loaded');
