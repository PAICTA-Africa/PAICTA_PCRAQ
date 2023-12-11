let milestoneCount = 1;

function addMilestone() {
    milestoneCount++;

    const milestonesDiv = document.getElementById('milestones');
    const newMilestoneDiv = document.createElement('div');
    newMilestoneDiv.className = 'milestone';

    newMilestoneDiv.innerHTML = `
    <label for="milestone_name_${milestoneCount}">Milestone Name:</label>
    <input type="text" id="milestone_name_${milestoneCount}" name="milestone_name[]" style="resize: none;" rows="5" class="form-control" required><br>

    <label for="milestone_description_${milestoneCount}">Milestone Description:</label>
    <textarea id="milestone_description_${milestoneCount}" name="milestone_description[]" style="resize: none;" rows="5" class="form-control" required></textarea><br><br>
    `;

    milestonesDiv.appendChild(newMilestoneDiv);
}