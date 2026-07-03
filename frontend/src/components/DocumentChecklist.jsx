import React, { useState } from 'react';

export default function DocumentChecklist({ groups, serviceId }) {
  const [checkedDocIds, setCheckedDocIds] = useState([]);
  const [collapsedGroups, setCollapsedGroups] = useState({});

  // Toggle checklist checkbox state
  const handleToggleDoc = (docId) => {
    setCheckedDocIds((prev) =>
      prev.includes(docId)
        ? prev.filter((id) => id !== docId)
        : [...prev, docId]
    );
  };

  // Toggle collapse state for a group
  const handleToggleCollapse = (groupId) => {
    setCollapsedGroups((prev) => ({
      ...prev,
      [groupId]: !prev[groupId]
    }));
  };

  // Evaluate if a group is satisfied based on checklist selections
  const isGroupSatisfied = (group) => {
    if (group.anyOne) {
      // satisfy if at least one doc in the group is checked
      return group.docs.some((doc) => checkedDocIds.includes(doc.id));
    } else {
      // satisfy if all mandatory docs in the group are checked
      const mandatoryDocs = group.docs.filter((doc) => doc.mandatory);
      if (mandatoryDocs.length === 0) return true;
      return mandatoryDocs.every((doc) => checkedDocIds.includes(doc.id));
    }
  };

  // Filter groups
  const mandatoryGroups = groups.filter((g) => g.mandatory);
  const totalMandatoryCount = mandatoryGroups.length;
  
  const satisfiedMandatoryGroups = mandatoryGroups.filter((g) => isGroupSatisfied(g));
  const satisfiedMandatoryCount = satisfiedMandatoryGroups.length;

  const isEligible = satisfiedMandatoryCount === totalMandatoryCount;
  const progressPercentage = totalMandatoryCount > 0
    ? Math.round((satisfiedMandatoryCount / totalMandatoryCount) * 100)
    : 100;

  // Determine status banner state
  let bannerClass = 'neutral';
  let bannerText = 'Apne checklist documents tick karke apply karne ki eligibility check karein.';

  if (checkedDocIds.length > 0) {
    if (isEligible) {
      bannerClass = 'success';
      bannerText = 'Saare jaruri documents upload karne ke liye ready hain. Aap apply karne ke liye bilkul eligible hain!';
    } else {
      const missingGroups = mandatoryGroups
        .filter((g) => !isGroupSatisfied(g))
        .map((g) => g.title);
      bannerClass = 'warning';
      bannerText = `Kuch jaruri documents missing hain. Kripya in groups me se document select karein: ${missingGroups.join(', ')}`;
    }
  }

  // Official portal link
  const portalUrl = `https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=${serviceId}&lang=en`;

  return (
    <div className="checklist-container">
      {/* 1. Header Progress Section */}
      <div className="checklist-progress-container">
        <div className="checklist-progress-header">
          <span className="checklist-progress-label">Jaruri documents ka completion state:</span>
          <span className="checklist-progress-percentage">{progressPercentage}%</span>
        </div>
        <div className="checklist-progress-bar-bg">
          <div
            className="checklist-progress-bar-fill"
            style={{ width: `${progressPercentage}%` }}
          ></div>
        </div>
        <div className="checklist-progress-fraction">
          {satisfiedMandatoryCount} of {totalMandatoryCount} groups completed
        </div>
      </div>

      {/* 2. Status Banner */}
      <div className={`checklist-status-banner ${bannerClass}`}>
        <span className="banner-icon">
          {bannerClass === 'success' ? '✅' : bannerClass === 'warning' ? '⚠️' : 'ℹ️'}
        </span>
        <span className="banner-text">{bannerText}</span>
      </div>

      {/* 3. Document Groups Cards */}
      <div className="checklist-groups-list">
        {groups.map((group) => {
          const isSatisfied = isGroupSatisfied(group);
          const isCollapsed = !!collapsedGroups[group.id];

          return (
            <div
              key={group.id}
              className={`checklist-group-card ${group.mandatory ? 'mandatory' : 'optional'} ${
                isSatisfied ? 'satisfied' : 'unsatisfied'
              }`}
            >
              {/* Group Card Header */}
              <div
                className="checklist-group-header"
                onClick={() => handleToggleCollapse(group.id)}
              >
                <div className="checklist-group-left">
                  <span className={`collapse-arrow ${isCollapsed ? 'collapsed' : 'expanded'}`}>
                    ▼
                  </span>
                  <div className="checklist-title-box">
                    <span className="group-title">{group.title}</span>
                    {group.anyOne && (
                      <span className="group-anyone-note">(Koi bhi EK praman patra upload karein)</span>
                    )}
                  </div>
                </div>

                <div className="checklist-group-right">
                  <span className={`group-satisfied-badge ${isSatisfied ? 'complete' : 'incomplete'}`}>
                    {isSatisfied ? 'Done' : 'Missing'}
                  </span>
                  <span className={`group-mandatory-badge ${group.mandatory ? 'required' : 'optional'}`}>
                    {group.mandatory ? 'Jaruri' : 'Optional'}
                  </span>
                </div>
              </div>

              {/* Collapsible Documents List */}
              {!isCollapsed && (
                <div className="checklist-docs-list">
                  {group.docs.map((doc) => {
                    const isDocChecked = checkedDocIds.includes(doc.id);

                    return (
                      <div
                        key={doc.id}
                        className={`checklist-doc-row ${isDocChecked ? 'checked' : ''}`}
                        onClick={() => handleToggleDoc(doc.id)}
                      >
                        <input
                          type="checkbox"
                          className="checklist-checkbox"
                          checked={isDocChecked}
                          onChange={() => {}} // Done via row onClick
                          onClick={(e) => e.stopPropagation()} // Prevent duplicate toggle
                        />
                        <span className="checklist-doc-name">{doc.name}</span>
                        <span
                          className={`checklist-doc-status-dot ${doc.mandatory ? 'required' : 'optional'}`}
                          title={doc.mandatory ? 'Jaruri (Mandatory)' : 'Chaho toh do (Optional)'}
                        ></span>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* 4. Actions Section */}
      <div className="checklist-actions">
        <a
          href={portalUrl}
          target="_blank"
          rel="noopener noreferrer"
          className={`checklist-apply-btn ${!isEligible ? 'disabled' : ''}`}
          onClick={(e) => {
            if (!isEligible) {
              e.preventDefault();
            }
          }}
        >
          Sewa Setu Portal par Apply karein
        </a>
        {!isEligible && (
          <div className="checklist-btn-warning">
            * Kripya apply karne ke liye saare jaruri (Jaruri) documents complete karein.
          </div>
        )}
      </div>
    </div>
  );
}
