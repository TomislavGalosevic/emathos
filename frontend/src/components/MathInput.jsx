import MathText from "./MathText";

export default function MathInput({ value, onChange, placeholder, rows = 3 }) {
  return (
    <div className="math-input">
      <textarea
        rows={rows}
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
      {value?.trim() && (
        <div className="math-preview">
          <span className="math-preview-label">Pregled</span>
          <MathText text={value} />
        </div>
      )}
    </div>
  );
}